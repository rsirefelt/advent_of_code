from functools import cmp_to_key

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines]
    return lines[:-1]

def parsePacketPairs(lines):
    idx = 0
    packet_pairs = []
    while idx < len(lines):
        packet1 = eval(lines[idx])
        packet2 = eval(lines[idx+1])
        packet_pairs.append((packet1, packet2))

        idx = idx + 3
    xxx = 3
    return packet_pairs

def arePacketsInRightOrder(packet1, packet2):
    if type(packet1) == int and type(packet2) == int:
        if packet1 < packet2:
            return 1
        if packet1 == packet2:
            return 0
        if packet1 > packet2:
            return -1

    if type(packet1) == list and type(packet2) == list:
        idx = 0
        while True:
            if idx >= len(packet1) and idx >= len(packet2):
                return 0
            if idx >= len(packet1):
                return 1
            if idx >= len(packet2):
                return -1
            comparison = arePacketsInRightOrder(packet1[idx], packet2[idx])
            if comparison == 1:
                return 1
            if comparison == -1:
                return -1
            idx = idx + 1

    if type(packet1) == int and type(packet2) == list:
        packet1 = [packet1]
        return arePacketsInRightOrder(packet1, packet2)
    if type(packet1) == list and type(packet2) == int:
        packet2 = [packet2]
        return arePacketsInRightOrder(packet1, packet2)

    assert False, "We should never get here!"
    return None

packet_pairs = parsePacketPairs(parseInput("input.txt"))
total_sum = 0
for idx, pair in enumerate(packet_pairs):
    if arePacketsInRightOrder(pair[0], pair[1]) == 1:
        #print("Pair " + str(idx+1) + ".")
        total_sum = total_sum + idx + 1
print("Part 1: " + str(total_sum))

packets = parseInput("input.txt")
packets = [eval(packet) for packet in packets if len(packet) > 0]
packets = sorted(packets, key=cmp_to_key(arePacketsInRightOrder), reverse=True)

prod = 1
for idx, packet in enumerate(packets):
    if packet == [[2]] or packet == [[6]]:
        prod = prod*(idx+1)
print("Part 2: " + str(prod))

xxx = 3
