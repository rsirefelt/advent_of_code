import re
import numpy as np


class Tile:
    def __init__(self, string_block):
        self.id = int(re.findall("([0-9]+)", string_block[0])[0])
        self.data = [
            [int(char) for char in line.replace("#", "1").replace(".", "0")]
            for line in string_block[1:]
        ]
        self.data = np.array([np.array(line) for line in self.data])

        self.sides = [
            self.data[0, :],
            self.data[:, 0],
            self.data[-1, :],
            self.data[:, -1],
        ]
        self.reversed_sides = [
            self.data[0, :][::-1],
            self.data[:, 0][::-1],
            self.data[-1, :][::-1],
            self.data[:, -1][::-1],
        ]
        self.sides = [list(side) for side in self.sides]
        self.reversed_sides = [list(side) for side in self.reversed_sides]
        self.matches = {}
        self.reversed_matches = {}

    def find_matches(self, tiles):
        # Check only 'unreversed' sides
        for idx, side in enumerate(self.sides):
            for tile_id, tile in tiles.items():
                if tile_id == self.id:
                    continue
                # print(side)
                if side in tile.sides:
                    self.matches[idx] = [tile_id, tile.sides.index(side)]
                if side in tile.reversed_sides:
                    self.reversed_matches[idx] = [
                        tile_id,
                        tile.reversed_sides.index(side),
                    ]

    def rotate(self):

        self.data = np.rot90(self.data)
        temp = {}
        temp_reversed = {}

        for key, val in self.matches.items():
            if key == 0:
                temp_reversed[1] = val
            if key == 1:
                temp[2] = val
            if key == 2:
                temp_reversed[3] = val
            if key == 3:
                temp[0] = val

        for key, val in self.reversed_matches.items():
            if key == 0:
                temp[1] = val
            if key == 1:
                temp_reversed[2] = val
            if key == 2:
                temp[3] = val
            if key == 3:
                temp_reversed[0] = val

        self.matches = temp
        self.reversed_matches = temp_reversed

    def rotation_times(self, x):
        for _ in range(x):
            self.rotate()

    def reverse_x(self):
        self.data = np.fliplr(self.data)
        temp = {}
        temp_reversed = {}

        for key, val in self.matches.items():
            if key == 0:
                temp_reversed[0] = val
            if key == 1:
                temp[3] = val
            if key == 2:
                temp_reversed[2] = val
            if key == 3:
                temp[1] = val

        for key, val in self.reversed_matches.items():
            if key == 0:
                temp[0] = val
            if key == 1:
                temp_reversed[3] = val
            if key == 2:
                temp[2] = val
            if key == 3:
                temp_reversed[1] = val
        self.matches = temp
        self.reversed_matches = temp_reversed


def process_map(matched_tiles, tiles):
    side_length = len(matched_tiles)

    for i, row in enumerate(matched_tiles):
        for j, element in enumerate(row):
            if element is None:
                break
            matches = element.matches
            reversed_matches = element.reversed_matches

            if j + 1 < side_length:
                if row[j + 1] is None:
                    # If next element can be matched directly to current alignment:
                    if 3 in matches:
                        elem_id, matching_side = matches[3]

                        new_element = tiles[elem_id]
                        handle_x(new_element, matching_side)
                        matched_tiles[i, j + 1] = new_element
                        # print(f"should match X normal: {matching_side}")
                        # print(element.data[:, -1])
                        # print(new_element.data[:, 0])

                        return
                    elif 3 in reversed_matches:
                        elem_id, matching_side = reversed_matches[3]

                        # Inverse the next element
                        new_element = tiles[elem_id]

                        handle_inversion_x(new_element, matching_side)
                        matched_tiles[i, j + 1] = new_element
                        # print(f"should match X reversed: {matching_side}")
                        # print(element.data[:, -1])
                        # print(new_element.data[:, 0])

                        return

            if i + 1 < side_length:
                if matched_tiles[i + 1, j] is None:
                    if 2 in matches:
                        elem_id, matching_side = matches[2]
                        new_element = tiles[elem_id]
                        # Shift matching side (to match y axis instead of x)
                        handle_y(new_element, matching_side)
                        matched_tiles[i + 1, j] = new_element
                        # print(f"should match Y normal: {matching_side}")
                        # print(element.data[-1, :])
                        # print(new_element.data[0, :])

                        return
                    elif 2 in reversed_matches:
                        elem_id, matching_side = reversed_matches[2]
                        # Inverse the next element
                        new_element = tiles[elem_id]

                        # Shift matching side (to match y axis instead of x)
                        handle_inversion_y(new_element, matching_side)

                        matched_tiles[i + 1, j] = new_element
                        # print(f"should match Y reversed: {matching_side}")
                        # print(element.data[-1, :])
                        # print(new_element.data[0, :])

                        return


def handle_x(new_element, matching_side):
    # Translate from X to 1
    if matching_side == 1:
        # Already matching in orientation
        pass
    elif matching_side == 0:
        # Translate from 0 --> 1
        # Reverse and rotate left
        new_element.reverse_x()
        new_element.rotation_times(1)
    elif matching_side == 2:
        # Translate from 2--> 1
        # Rotate right (a.k.a. left 3 times).
        new_element.rotation_times(3)
    elif matching_side == 3:
        # Translate from 3 --> 1
        # Rotate left, flip , rotate left again.
        new_element.rotation_times(1)
        new_element.reverse_x()
        new_element.rotation_times(1)


def handle_y(new_element, matching_side):
    # Translate from X to 0.
    if matching_side == 0:
        # Already matching in orientation
        pass
    elif matching_side == 1:
        # Rotate right and flip (when x axis is aligned)
        new_element.rotation_times(1)
        new_element.reverse_x()
        new_element.rotation_times(2)
    elif matching_side == 2:
        new_element.rotation_times(2)
        new_element.reverse_x()
    elif matching_side == 3:
        # Rotate left
        new_element.rotation_times(1)


def handle_inversion_x(new_element, matching_side):
    # Translate from -X to 1
    if matching_side == 0:
        new_element.rotation_times(1)
    if matching_side == 1:
        new_element.rotation_times(3)
        new_element.reverse_x()
        new_element.rotation_times(1)
    if matching_side == 2:
        new_element.rotation_times(3)
    if matching_side == 3:
        new_element.rotation_times(2)


def handle_inversion_y(new_element, matching_side):
    # Translate from -X to 0.
    if matching_side == 0:
        new_element.reverse_x()
    if matching_side == 1:
        new_element.rotation_times(3)
    if matching_side == 2:
        new_element.rotation_times(2)
    if matching_side == 3:
        new_element.rotation_times(1)
        new_element.reverse_x()


def find_monsters(map_):

    # Parse monster
    with open("monster") as f:
        lines = [line for line in f.readlines()]

    monster = []
    for line in lines:
        line = line.replace("\n", "")
        monster.append([int(c) for c in line.replace(" ", "0").replace("#", "1")])

    monster = np.array(monster)

    # rotate and flip map
    for _ in range(4):
        map_ = np.rot90(map_)
        for _ in range(2):
            map_ = np.fliplr(map_)
            monster_count = 0

            # Loop over each "monster-sized" chunk
            for y in range(len(map_) - 3):
                for x in range(len(map_) - 20):
                    possible_monster = map_[y : y + 3, x : x + 20]
                    # Check if monster exists by multiplying monster with chunk
                    monster_check = np.multiply(possible_monster, monster)

                    # Monster exists if result is equal to the monster (i.e. "and" every 1)
                    if np.array_equal(monster_check, monster):
                        monster_count += 1

            # Calculate number of ones that do not belong to monsters.
            if monster_count:
                monster_enties = monster_count * np.count_nonzero(monster)
                count = np.count_nonzero(map_) - monster_enties

                return count


def match_to_map(tiles):
    square_side = int(np.sqrt(len(tiles)))
    matched_tiles = np.full((square_side, square_side), None)

    # Each tile-link is defined as:
    #     0
    #   #####
    #   #####
    # 1 #####  3
    #   #####
    #   #####
    #     2
    corners = [
        tile
        for tile in tiles.values()
        if len(tile.matches) + len(tile.reversed_matches) == 2
    ]

    # Pick corner and align it (done manually, but need to flip to that 2,3 in matched)
    corner = corners[0]

    # Place corner as start point.
    matched_tiles[0][0] = corner

    # Get size of square per tile.
    tile_side = len(corners[0].data)

    # Match all tiles into map
    while None in matched_tiles:
        process_map(matched_tiles, tiles)

    # Remove borders (thus reduce map size)
    tile_side = tile_side - 2
    # Create map
    map_ = np.full((square_side * tile_side, square_side * tile_side), None)

    # Place each tile into map (based on current orientation)
    for i, row in enumerate(matched_tiles):
        for j, elem in enumerate(row):
            # print(f"{i}, {j} : {elem.id} {elem.matches} {elem.reversed_matches}")
            start_x = i * tile_side
            end_x = (i + 1) * tile_side
            start_y = j * tile_side
            end_y = (j + 1) * tile_side

            map_[start_x:end_x, start_y:end_y] = elem.data[1:-1, 1:-1]

    return map_


def task1(tiles):
    corners = [
        tile
        for tile in tiles.values()
        if len(tile.matches) + len(tile.reversed_matches) == 2
    ]
    res = 1
    for corner in corners:
        res *= corner.id
    return res


if __name__ == "__main__":
    tiles = {}
    with open("input") as f:
        lines = list(f.readlines())
        string_block = []
        for line in lines:
            line = line.rstrip()
            if line == "":
                tile = Tile(string_block)
                tiles[tile.id] = tile
                string_block = []
            else:
                string_block.append(line)

    for tile in tiles.values():
        tile.find_matches(tiles)

    print(f"Result task 1: {task1(tiles)}")

    map_ = match_to_map(tiles)

    print(f"Result task 2: {find_monsters(map_)}")
