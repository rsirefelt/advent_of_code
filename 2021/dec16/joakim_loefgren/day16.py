from dataclasses import dataclass
import operator
import functools


def parse_input(file_path):
    with open(file_path, 'r') as f:
        text = f.read().strip()
    return text


@dataclass
class Packet:
    version: int
    type_id: int


@dataclass
class LiteralPacket(Packet):
    literal: int
    length: int

    def __len__(self):
        return self.length


@dataclass
class OperatorPacket(Packet):
    len_type_id: int
    contents: list

    def __len__(self):
        res = 7
        if self.len_type_id == 0:
            res += 15
        else:
            res += 11
        for subpac in self.contents:
                res += subpac.__len__()
        return res


class Decoder:
    def __init__(self, transmission):
        if isinstance(transmission, int):
            transmission = hex(transmission)[2:]
        width = len(transmission) * 4
        self.transmission = f"{int(transmission, 16):0>{width}b}"
        self.pos = 0

    def read_bits(self, num):
        pos_new = self.pos + num
        bits = self.transmission[self.pos : pos_new]
        self.pos = pos_new
        return bits

    def parse_header(self):
        header = self.read_bits(6)
        version = int(header[:3], 2)
        type_id = int(header[3:], 2)
        return version, type_id

    def parse_len_type_id(self):
        len_type_id = self.read_bits(1)
        return int(len_type_id, 2)

    def parse_literal(self):
        bit_first = 1
        bits_digit = ''
        count = 0
        while bit_first == 1:
            count += 1
            bits = self.read_bits(5)
            bit_first = int(bits[0])
            bits_digit += bits[1:]

        digit = int(bits_digit, 2)
        return digit, len(bits_digit) + count

    def parse_sub_length(self):
        sub_length = self.read_bits(15)
        return int(sub_length, 2)
    
    def parse_sub_number(self):
        sub_number = self.read_bits(11)
        return int(sub_number, 2)

    def parse_packet(self):
        version, type_id = decoder.parse_header()
        if type_id == 4:  # literal packet
            lit, len_lit = self.parse_literal()
            len_ = 6 + len_lit
            packet = LiteralPacket(version, type_id, lit, len_)
        else:
            len_type_id = self.parse_len_type_id()
            if len_type_id == 0:
                len_sub = self.parse_sub_length()
                contents = []
                while len_sub > 0:
                    contents.append(self.parse_packet())
                    len_sub -= len(contents[-1])
            elif len_type_id == 1:
                num_sub = self.parse_sub_number()
                contents = [self.parse_packet() for _ in range(num_sub)]
            else:
                raise ValueError
            packet = OperatorPacket(version, type_id, len_type_id, contents)
        return packet 


def sum_versions(packet):
    res = packet.version
    if isinstance(packet, OperatorPacket):
        for subpac in packet.contents:
            res += sum_versions(subpac)
    return res


def prod(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return functools.reduce(operator.mul, numbers)


def extend_operator(op):
    functools.wraps(op)
    def wrapper(args):
        return functools.reduce(op, args)
    return wrapper


class Evaluator:
    OPERATIONS = {
        0: sum,
        1: prod,
        2: min,
        3: max,
        5: extend_operator(operator.gt),
        6: extend_operator(operator.lt),
        7: extend_operator(operator.eq),
    }
    def __call__(self, packet):
        if isinstance(packet, LiteralPacket):
            res = packet.literal
        else:
            operation = self.OPERATIONS[packet.type_id]
            res = operation([self.__call__(subpac) for subpac in packet.contents])
        return res


if __name__ == '__main__':
    transmission = parse_input('./input_day16.txt')
    decoder = Decoder(transmission)
    packet = decoder.parse_packet()

    # Part I
    print(sum_versions(packet))

    # Part II 
    evaluator = Evaluator()
    res = evaluator(packet)
    print(res)
