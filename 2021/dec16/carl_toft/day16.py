import numpy as np
from utils import read_lines

hex_to_binary = {'0' : '0000',  '1' : '0001', '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'
    }

class Packet():
    def __init__(self, version=None, packet_type=None, literal=None):
        self.sub_packets = []
        self.version = version
        self.packet_type = packet_type
        self.literal = literal

    def compute(self):
        if self.literal is not None:
            return self.literal

        values = np.array([packet.compute() for packet in self.sub_packets], dtype=int)
        if self.packet_type == 0:
            return np.sum(values)
        elif self.packet_type == 1:
            return np.prod(values)
        elif self.packet_type == 2:
            return np.min(values)
        elif self.packet_type == 3:
            return np.max(values)
        elif self.packet_type == 5:
            if values[0] > values[1]:
                return 1
            else:
                return 0
        elif self.packet_type == 6:
            if values[0] < values[1]:
                return 1
            else:
                return 0
        elif self.packet_type == 7:
            if values[0] == values[1]:
                return 1
            else:
                return 0

def parsePacket(data, idx):
    """Parse the packet starting at the given index."""
    version = int(data[idx:idx + 3], 2)
    idx = idx + 3

    packet_type = int(data[idx:idx+3], 2)
    idx = idx + 3

    # If the packet contains a literal, parse it
    if packet_type == 4:
        literal = ''
        last_value = False
        while not last_value:
            last_value = data[idx] == '0'
            literal = literal + data[idx+1:idx+5]
            idx = idx + 5
        literal = int(literal, 2)

        # We are done parsing the literal packet!
        return Packet(version=version, packet_type=packet_type, literal=literal), idx
    else:
        # The packet contains subpackets.
        packet = Packet(version=version, packet_type=packet_type)

        # Parse the subpackets
        length_type = int(data[idx])
        if length_type == 0:
            sub_packet_length = int(data[idx+1:idx+16], 2)
            idx = idx + 16
        else:
            sub_packet_length = int(data[idx+1:idx+12], 2)
            idx = idx + 12

        num_packets_parsed = 0
        num_bits_parsed = 0

        done = False
        while not done:
            subpacket, new_idx = parsePacket(data, idx)
            num_bits_parsed = num_bits_parsed + (new_idx - idx)
            num_packets_parsed = num_packets_parsed + 1
            packet.sub_packets.append(subpacket)

            idx = new_idx

            if length_type == 0 and num_bits_parsed >= sub_packet_length:
                done = True
            if length_type == 1 and num_packets_parsed >= sub_packet_length:
                done = True

        return packet, idx


def versionSum(packet):
    sum = packet.version
    for subpacket in packet.sub_packets:
        sum = sum + versionSum(subpacket)
    return sum


# Read the input data
data = read_lines("/home/carl/Code/AdventOfCode/Day16/input.txt")[0]
data = ''.join([hex_to_binary[char] for char in data])

# Parse the packets
packet, idx = parsePacket(data, 0)

print("Part 1:", versionSum(packet))
print("Part 2:", packet.compute())