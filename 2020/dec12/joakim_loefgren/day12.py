""" Advent of Code Day 12 """

import numpy as np


class Ship:

    ORIENTATIONS = {"N": 0, "E": 1, "S": 2, "W": 3}
    ROT90 = np.array([[0, -1], [1, 0]])

    def __init__(self, pos=[0, 0], pos_waypoint=[10, 1], orientation=1):
        self.pos = np.asarray(pos, np.int64)
        self.pos_waypoint = np.asarray(pos_waypoint, np.int64)
        self.orientation = 1
        self.instructions = []

    def load_instructions(self, input_file):
        with open(input_file, "r") as fp:
            for line in fp:
                self.instructions.append((line[0], int(line[1:])))

    def reset(self):
        self.orientation = 1
        self.pos = np.asarray([0, 0])
        self.pos_waypoint = np.asarray([10, 1])

    def move(self, pos, dist, orientation=None):
        if orientation is None:
            orientation = self.orientation
        if orientation == 0:
            pos[1] += dist
        elif orientation == 1:
            pos[0] += dist
        elif orientation == 2:
            pos[1] -= dist
        elif orientation == 3:
            pos[0] -= dist

    def turn(self, hand, deg):
        if hand == "R":
            self.orientation = (self.orientation + deg // 90) % 4
        elif hand == "L":
            self.orientation = (self.orientation - deg // 90) % 4

    def navigate_solo(self):
        for name, num in self.instructions:
            orient = self.ORIENTATIONS.get(name, None)
            if orient is not None:
                self.move(self.pos, num, orient)
            elif name == "F":
                self.move(self.pos, num)
            elif name in ["L", "R"]:
                self.turn(name, num)
            else:
                raise ValueError("Invalid instruction.")

    def rotate_waypoint(self, hand, deg):
        n = deg // 90
        if hand == "R":
            sgn = -1
        elif hand == "L":
            sgn = 1
        rot = np.linalg.matrix_power(sgn * self.ROT90, n)
        self.pos_waypoint = rot @ self.pos_waypoint

    def move_to_waypoint(self, num):
        self.pos += self.pos_waypoint * num

    def navigate_waypoint(self):
        for name, num in self.instructions:
            orient = self.ORIENTATIONS.get(name, None)
            if orient is not None:
                self.move(self.pos_waypoint, num, orient)
            elif name == "F":
                self.move_to_waypoint(num)
            elif name in ["L", "R"]:
                self.rotate_waypoint(name, num)
            else:
                raise ValueError("Invalid instruction.")

    def norm_manhattan(self):
        return np.sum(np.abs(self.pos))


if __name__ == "__main__":

    ship = Ship()
    ship.load_instructions("./input_day12.txt")

    # Part I
    ship.navigate_solo()
    print(ship.norm_manhattan())

    # Part II
    ship.reset()
    ship.navigate_waypoint()
    print(ship.norm_manhattan())
