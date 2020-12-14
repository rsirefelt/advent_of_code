import re


def set_bits(val, offsets):
    for offset in offsets:
        val = val | 1 << offset
    return val


def clear_bits(val, offsets):
    for offset in offsets:
        val = val & ~(1 << offset)
    return val


# Part 1
def apply_mask(val, mask):
    bits2clear = [len(mask) - i - 1 for i, letter in enumerate(mask) if letter == "0"]
    bits2set = [len(mask) - i - 1 for i, letter in enumerate(mask) if letter == "1"]

    val = clear_bits(val, bits2clear)
    val = set_bits(val, bits2set)
    return val


memory = dict()
with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.rstrip().split(" = ")
        if line[0] == "mask":
            mask = line[1]
        else:
            val = apply_mask(int(line[1]), mask)
            address = int(re.match(r"mem\[(\d+)\]", line[0]).groups()[0])
            memory[address] = val

print(f"1) Sum of values {sum(memory.values())}")

# Part 2
def gen_addresses(address, bits2float):
    addresses = [address]
    for float_bit in bits2float:
        for addr in addresses:
            addresses.append(addr ^ (1 << float_bit))

    return addresses


def get_addresses(address, mask):
    bits2set = [len(mask) - i - 1 for i, letter in enumerate(mask) if letter == "1"]
    bits2float = [len(mask) - i - 1 for i, letter in enumerate(mask) if letter == "X"]
    address = set_bits(address, bits2set)
    new_addresses = [address]
    for float_bit in bits2float:
        old_addresses = new_addresses.copy()
        for addr in old_addresses:
            new_addresses.append(addr ^ (1 << float_bit))

    return new_addresses


memory = dict()
with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.rstrip().split(" = ")
        if line[0] == "mask":
            mask = line[1]
        else:
            val = int(line[1])
            address = int(re.match(r"mem\[(\d+)\]", line[0]).groups()[0])
            addresses = get_addresses(address, mask)
            memory_update = dict.fromkeys(addresses, val)
            memory.update(memory_update)


print(f"2) Sum of values {sum(memory.values())}")
