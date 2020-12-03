import numpy as np


def traverse(row_add, col_add, lines):
  n_rows, n_cols = lines.shape
  n_trees = 0
  row = col = 0
  while True:
    if row >= n_rows:
      break
    if lines[row][col] == 1:
      n_trees += 1

    row += row_add
    col = (col + col_add) % n_cols

  return n_trees


with open("input.txt") as f:
  lines = f.read().replace('.', '0').replace('#', '1').splitlines()
  lines = [list(map(lambda char: char, line)) for line in lines]

lines = np.array(lines, dtype=int)
print(lines)
print(lines.shape)

moves = [
  (1, 1),
  (1, 3),
  (1, 5),
  (1, 7),
  (2, 1),
]
tot_trees = 1
for row_move, col_move in moves:
  n_trees = traverse(row_move, col_move, lines)
  print(n_trees)
  tot_trees *= n_trees

print(tot_trees)
