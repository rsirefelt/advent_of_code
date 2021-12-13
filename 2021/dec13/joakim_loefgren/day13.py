import numpy as np


def parse_input(file_path): 
    with open(file_path, 'r') as f:
        text = f.read()
        tsplit = text.split('\n\n')
        coords_raw = tsplit[0]
        instructions_raw = tsplit[1]
        coords = np.array([np.fromstring(l, sep=',') for l in coords_raw.split()], dtype=int)
        instructions = []
        for line in instructions_raw.splitlines():
            lsplit = line.split(' ')[2].split('=')
            instructions.append((lsplit[0], int(lsplit[1])))
    return coords, instructions


def fold(paper, along):
    axis, line = along
    if axis == 'y':
        base = paper[:line, :]
        overlay = paper[line + 1:, :]
        overlay = np.flip(overlay, axis=0)
        paper_folded = base | overlay
    elif axis == 'x':
        base = paper[:, line + 1:]
        overlay = paper[:, :line]
        overlay = np.fliplr(overlay)
        paper_folded = base | overlay
    return paper_folded


def visualize(paper):
    art = ''
    for line in paper:
        art += ''.join(['#' if c else '.' for c in line])
        art += '\n'
    return art


if __name__ == '__main__':
    coords, instructions = parse_input('./input_day13.txt')
    # coords, instructions = parse_input('./test.txt')
    paper = np.zeros((np.max(coords[:, 1]) + 1, np.max(coords[:, 0]) + 1), dtype=bool) 
    paper[coords[:, 1], coords[:, 0]] = True  

    # Part I 
    paper_folded = fold(paper, along=instructions[0])
    print(np.sum(paper_folded))

    # Part II
    for instr in instructions:
        paper = fold(paper, along=instr)

    print(visualize(np.fliplr(paper)))
