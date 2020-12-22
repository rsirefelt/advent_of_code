import numpy as np


def parse_input(input_file):

    with open(input_file, "r") as fp:
        tiles_raw = fp.read().split("\n\n")

    tiles = {}
    trans = str.maketrans({".": "0 ", "#": "1 "})
    for t_raw in tiles_raw:
        rows = t_raw.split("\n")
        key = int(rows[0][5:-1])
        tiles[key] = np.array(
            [
                np.fromstring(row.translate(trans), dtype=np.int64, sep=" ")
                for row in rows[1:] if len(row) > 1
            ]
        )
    return tiles


def get_all_borders(tiles):
    borders = {}
    for key in tiles:
        borders[key] = _get_borders(tiles, key)
    return borders


def order_tiles(tiles):
    borders = get_all_borders(tiles)
    keys = list(tiles.keys())
    ntiles = len(keys)
    nrows = int(np.sqrt(ntiles))

    # find all tile pairs with a matching border
    matches = np.zeros((ntiles, ntiles), np.int64)
    prod = 1
    for i in range(ntiles):
        for j in range(i + 1, ntiles):
            borders_i = borders[keys[i]]
            borders_j = borders[keys[j]]
            if _match_borders(borders_i, borders_j):
                matches[i, j] = 1
                matches[j, i] = 1

    # Assemble the tiles row by row starting from a corner
    icorners = np.argwhere(matches.sum(axis=0) == 2).flatten()
    tile_order = np.zeros((nrows, nrows), np.int64)
    visited = []

    # first row
    ifirst = icorners[0]
    tile_order[0, 0] = ifirst
    visited.append(ifirst)
    inext = ifirst
    for j in range(1, nrows):
        inext = next(
            i for i in range(ntiles)
            if (matches[inext, i] == 1 and i not in visited 
                and matches[i, :].sum() <=3)
        )
        tile_order[0, j] = inext
        visited.append(inext)

    # subsequent rows
    for k in range(1, nrows):
        ifirst = next(
            i for i in range(ntiles) 
            if (matches[ifirst, i] == 1 and i not in visited 
                and matches[i, :].sum() <=3)
        )
        tile_order[k, 0] = ifirst
        visited.append(ifirst)
        inext = ifirst
        for j in range(1, nrows):
            inext = next(
                i for i in range(ntiles) 
                if (matches[inext, i] == 1 and i not in visited 
                    and matches[i, visited].sum() == 2)
            )
            tile_order[k, j] = inext
            visited.append(inext)

    to_keys = np.vectorize(lambda x: keys[x])
    return to_keys(tile_order)


def build_image(tiles, tiles_ordered, binary=True, spaced=False, skip_borders=True):
    side = tiles[tiles_ordered[0, 0]].shape[0]
    if skip_borders:
        side -= 2
    nrows = tiles_ordered.shape[0]
    image = np.zeros((side*nrows, side*nrows), dtype=np.int64)
    for i in range(nrows):
        for j in range(nrows):
            tile = tiles[tiles_ordered[i, j]]
            if skip_borders:
                part = tile[1:-1, 1:-1]
            else:
                part = tile
            image[side*i:side*(i+1), side*j: side*(j +1)] = part

    if not binary:
        subs = {0: ".", 1: "#"}
        image_str = ""
        if not spaced:
            for row in image:
                image_str += "".join([subs[c] for c in row]) + '\n'
        else:
            for irow, row in enumerate(image):
                for isid in range(nrows):
                    image_str += "".join([subs[c] for c in row[isid*side:side*(isid + 1)]])
                    image_str += ' '
                image_str += '\n'
                if (irow + 1) % side == 0:
                    image_str += '\n'
        image = image_str
    return image


def _match_borders(borders1, borders2):
    for i, bi in enumerate(borders1):
        for j, bj in enumerate(borders2):
            if np.array_equal(bi, bj):
                rev = 0
                return i, j, rev
            elif np.array_equal(bi, bj[::-1]):
                rev = 1
                return i, j, rev
    return False


def _get_borders(tiles, key):
    tile = tiles[key]
    borders = np.array([tile[0, :], tile[:, 0], tile[-1, :], tile[:, -1]])
    return borders


def orient_tiles(tiles, tiles_ordered):
    # orient the top left corner tile
    nrows = tiles_ordered.shape[0]
    key_curr = tiles_ordered[0, 0]
    key_right = tiles_ordered[0, 1]
    borders_curr = _get_borders(tiles, key_curr)
    borders_right = _get_borders(tiles, key_right)
    i, j, rev = _match_borders(borders_curr, borders_right)
    if i != 3:
        tiles[key_curr] = np.rot90(tiles[key_curr], k=3-i)

    key_down = tiles_ordered[1, 0]
    borders_curr = _get_borders(tiles, key_curr)
    borders_down = _get_borders(tiles, key_down)
    i, j, rev = _match_borders(borders_curr, borders_down)
    if i != 2:
        tiles[key_curr] = np.flipud(tiles[key_curr])

    # orient remaining tiles in first row
    nrots = {0: 1, 2: 3, 3: 2, 1: 0}
    for icol in range(1, nrows):
        key_curr = tiles_ordered[0, icol]
        key_left = tiles_ordered[0, icol-1]
        borders_curr = _get_borders(tiles, key_curr)
        borders_left = _get_borders(tiles, key_left)
        i, j, rev = _match_borders(borders_curr, borders_left)
        k = nrots[i]
        if k:
            tiles[key_curr] = np.rot90(tiles[key_curr], k=k)
        borders_curr = _get_borders(tiles, key_curr)
        borders_left = _get_borders(tiles, key_left)
        if not (np.array_equal(borders_curr[1, :], borders_left[3, :])):
            tiles[key_curr] = np.flipud(tiles[key_curr])

    # orient remaning rows
    nrots = {0: 0, 1: 3, 3: 1, 2: 2}
    for irow in range(1, nrows):
        for icol in range(0, nrows):
            key_curr = tiles_ordered[irow, icol]
            key_up = tiles_ordered[irow-1, icol]
            borders_curr = _get_borders(tiles, key_curr)
            borders_up = _get_borders(tiles, key_up)
            i, j, rev = _match_borders(borders_curr, borders_up)
            k = nrots[i]
            if k:
                tiles[key_curr] = np.rot90(tiles[key_curr], k=k)

            borders_curr = _get_borders(tiles, key_curr)
            borders_up = _get_borders(tiles, key_up)
            if not (np.array_equal(borders_curr[0, :], borders_up[2, :])):
                tiles[key_curr] = np.fliplr(tiles[key_curr])


def load_seamonster(input_file='./seamonster.txt'):
    trans = str.maketrans({" ": "0 ", "#": "1 "})
    with open(input_file) as fp:
        lines = fp.read().splitlines()
        seamonster = np.array(
            [np.fromstring(line.translate(trans), dtype=np.int64, sep=" ")
             for line in lines
            ], dtype=np.bool
        )
    return seamonster


def find_water_roughness(image):
    seamonster = load_seamonster()
    image = image.copy()
    mx, my = image.shape
    monst = seamonster
    for nrot in [0, 1, 2, 3]:
        for flip in [False, np.flipud, np.fliplr]:
            if nrot:
                monst = np.rot90(monst, k=nrot)
            if flip:
                monst = flip(monst)
            sx, sy = monst.shape
            for i in range(mx - sx):
                for j in range(my - sy):
                    if np.all(image[i:i+sx,j:j+sy][monst] == 1):
                        image[i:i+sx,j:j+sy][monst] = 0
    return np.sum(image)


if __name__ == "__main__":
    tiles = parse_input("./input_day20.txt")
    tiles_ordered = order_tiles(tiles)
    orient_tiles(tiles, tiles_ordered)

    # Part I
    print(
        tiles_ordered[0, 0] * tiles_ordered[-1, 0]
        * tiles_ordered[-1, -1] * tiles_ordered[0, -1]
    )
    # Part II
    image = build_image(tiles, tiles_ordered, binary=True)
    print(find_water_roughness(image))
