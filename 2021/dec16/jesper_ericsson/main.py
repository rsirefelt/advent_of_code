import numpy as np
import time


def readData():
    filename = "testdata.csv"
    # filename = "data.csv"
    with open(filename, "r") as f:
        input = f.readline().rstrip()
    f.close()

    transmission = ""
    for char in input:
        print(int(char, base=16))
        transmission += bin(int(char, 16))[2:].zfill(4)

    return transmission

def get_literal_value(packet):
    


def evaluate_packet(packet):
    packet_version = int(packet[0:3], 2)
    packet_type = int(packet[3:6], 2)

    if packet_type == 4:
        get_literal_value(packet[6:])


    return (packet_version, packet_type)


def prob1(transmission):
    pac_vers, pac_type = evaluate_packet(transmission)
    print(pac_vers, pac_type)


def prob2(wires, segments):
    print("Problem 2 sum of all values:", sum_values)


def main():
    transmission = readData()
    print(transmission)

    prob1(transmission)
    # prob2(wires, segments)


if __name__ == "__main__":
    main()
