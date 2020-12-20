from typing import OrderedDict

import numpy as np
from scipy.ndimage import correlate

tiles = OrderedDict()
tile_id = None
imtile = []
with open('inputs/day20') as f:
    for line in f:
        if line.startswith('Tile'):
            tile_id = int(line.rstrip().split(' ')[1][:-1])
            continue
        elif line != '\n':
            row = line.rstrip()
            imrow = np.array([c == '#' for c in row])
            imtile.append(imrow)
            continue
        tiles[tile_id] = np.array(imtile)
        imtile = []

tiles[tile_id] = np.array(imtile)


def get_edges(im):
    edges = list()
    edges.append(im[0, :])
    edges.append(im[-1, :])
    edges.append(im[:, 0])
    edges.append(im[:, -1])
    edges.append(im[0, :][::-1])
    edges.append(im[-1, :][::-1])
    edges.append(im[:, 0][::-1])
    edges.append(im[:, -1][::-1])

    return edges


def count_matches(ed1, ed2):
    m = 0
    for e1 in ed1:
        hasmatch = False
        for e2 in ed2:
            if (e1 == e2).all():
                hasmatch = True
                break
        if hasmatch:
            m += 1
    return m


available_matches = np.zeros((len(tiles), len(tiles)))
i = 0
for id, im in tiles.items():
    edges = get_edges(im)
    j = 0
    for id2, im2 in tiles.items():
        if id != id2:
            edges2 = get_edges(im2)
            available_matches[i, j] = count_matches(edges, edges2)
        j += 1
    i += 1

indices_with_two_matches = np.where((available_matches > 0).sum(axis=0) == 2)[0]
prod = 1
for index, id in enumerate(tiles.keys()):
    if index in indices_with_two_matches:
        prod *= id

print(f'a) {prod}')


sidelen = int(np.sqrt(len(tiles)))
tile_ims = list(tiles.values())
starting_index = indices_with_two_matches[0]


def apply_flip_rot(im, fliprot):
    if fliprot[0] == 1:
        im = np.fliplr(im)
    if fliprot[1] == 1:
        im = np.flipud(im)
    for _ in range(fliprot[2]):
        im = np.rot90(im)
    return im


def place_tile(puzzle, puzzle_as_inds, pos, tile_ind):
    top_to_match = None
    if pos[0] > 0:
        top_to_match = puzzle[pos[0]-1, pos[1], -1, :]
    left_to_match = None
    if pos[1] > 0:
        left_to_match = puzzle[pos[0], pos[1] - 1, :, -1]

    for fliplr in range(2):
        for fliptb in range(2):
            for rot in range(4):
                imrot = apply_flip_rot(tile_ims[tile_ind], [fliplr, fliptb, rot])
                if not (left_to_match is None or (imrot[:, 0] == left_to_match).all()):
                    continue
                if not (top_to_match is None or (imrot[0, :] == top_to_match).all()):
                    continue

                puzzle[pos[0], pos[1], :, :] = imrot
                puzzle_as_inds[pos[0], pos[1]] = tile_ind
                return True
    return False


def init_board(puzzle, puzzle_as_inds, ind):
    # initialize board by finding a corner triplet that fits
    puzzle_as_inds[0, 0] = ind
    starting_tile = tile_ims[ind]
    matches = np.where(available_matches[ind, :] > 0)[0]
    for fliplr in range(2):
        for fliptb in range(2):
            for rot in range(4):
                im = apply_flip_rot(starting_tile, [fliplr, fliptb, rot])
                puzzle[0, 0, :, :] = im

                success = place_tile(puzzle, puzzle_as_inds, (0, 1), matches[0])
                if success:
                    success = place_tile(puzzle, puzzle_as_inds, (1, 0), matches[1])

                if not success:
                    success = place_tile(puzzle, puzzle_as_inds, (1, 0), matches[0])
                    if success:
                        success = place_tile(puzzle, puzzle_as_inds, (0, 1), matches[1])

                if success:
                    return True
    return False


puzzle = np.zeros((sidelen, sidelen, tile_ims[0].shape[0], tile_ims[0].shape[1]))
puzzle_as_inds = -1*np.ones((sidelen, sidelen), dtype=np.int)
# tiles can be flipped and rotated. This means that we can start from any border and build from there
assert init_board(puzzle, puzzle_as_inds, starting_index)

for i in range(sidelen):
    for j in range(sidelen):
        if puzzle_as_inds[i, j] >= 0:  # alread placed
            continue

        # get possible pieces to place
        matches_top = None
        if i > 0:
            ind = puzzle_as_inds[i-1, j]
            matches_top = set(np.where(available_matches[ind, :] > 0)[0])
        matches_left = None
        if j > 0:
            ind = puzzle_as_inds[i, j-1]
            matches_left = set(np.where(available_matches[ind, :] > 0)[0])

        if matches_left is None:
            matches = set(matches_top)
        elif matches_top is None:
            matches = set(matches_left)
        else:
            matches = matches_left.intersection(matches_top)

        success = False
        for ind in matches:
            success = place_tile(puzzle, puzzle_as_inds, (i, j), ind)
            if success:
                break

        assert success

tileside = puzzle.shape[2]-2
im_side = sidelen*tileside
puzzle_im = np.zeros((im_side, im_side), dtype=np.int)

for i in range(sidelen):
    for j in range(sidelen):
        puzzle_im[tileside*i:tileside*(i+1), tileside*j:tileside*(j+1)] = puzzle[i, j, 1:-1, 1:-1]


monsterfilter = list()
monsterfilter.append(np.array([c == '#' for c in '                  # ']))
monsterfilter.append(np.array([c == '#' for c in '#    ##    ##    ###']))
monsterfilter.append(np.array([c == '#' for c in ' #  #  #  #  #  #   ']))
monsterfilter = np.array(monsterfilter).astype(np.int)
monstersize = monsterfilter.sum()

max_monsters = 0
water_roughness = 0
for fliplr in range(2):
    for fliptb in range(2):
        for rot in range(4):
            im = apply_flip_rot(puzzle_im, [fliplr, fliptb, rot])
            monstercount = (correlate(im, monsterfilter, mode='constant', cval=0) == monstersize).sum()
            if monstercount > max_monsters:
                max_monsters = monstercount
                water_roughness = im.sum() - monstercount*monstersize  # assume no overlapping monsters

print(f'b) {water_roughness}')
