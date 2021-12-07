import numpy as np
import time


def prob1(crab_positions):
    num_positions = np.max(crab_positions)

    min_fuel_cost = 1000000
    position = num_positions + 1
    for i in range(num_positions):
        fuel_cost = np.sum(np.absolute(crab_positions - i))
        if fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost
            position = i
    print("Fuel cost", min_fuel_cost, "at position", position)


def prob2(crab_positions):
    num_positions = np.max(crab_positions)

    min_fuel_cost = 100000000
    position = 1000000000

    for i in range(num_positions):
        distance_new_positions = np.absolute(crab_positions - i)
        fuel_cost = np.sum(distance_new_positions * (distance_new_positions + 1) * 0.5)
        # print("Fuel cost", fuel_cost, "at position", i)
        if fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost
            position = i
    print("Fuel cost", min_fuel_cost, "at position", position)


def main():
    input_data = np.genfromtxt("testdata.csv", dtype=int, delimiter=",")
    input_data = np.genfromtxt("data.csv", dtype=int, delimiter=",")

    start = time.time()
    prob1(input_data)
    end = time.time()
    print(["Naive solution: ", end - start])

    start = time.time()
    prob2(input_data)
    end = time.time()
    print(["Speed up: ", end - start])


if __name__ == "__main__":
    main()
