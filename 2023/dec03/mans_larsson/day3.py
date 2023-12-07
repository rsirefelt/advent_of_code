import numpy as np
import re

rows = []
special_symbol_map = []
gear_map = []
with open('inputs/day3') as f:
    for line in f:
        rows.append(line.rstrip())
        special_symbol_map.append(np.array([not c.isnumeric() and c != '.' for c in line.rstrip()]))
        gear_map.append(np.array([c == '*' for c in line.rstrip()]))
special_symbol_map = np.stack(special_symbol_map)

gear_map = np.stack(gear_map)
gear_count = np.zeros_like(gear_map, dtype='int')
gear_number = np.ones_like(gear_map, dtype='int')

engine_sum = 0
for i, row in enumerate(rows):
    for m in re.finditer(r'\d+', row):
        row_low = max(0, i-1)
        row_high = min(special_symbol_map.shape[0], i+2)
        col_low = max(0, m.span()[0]-1)
        col_high = min(special_symbol_map.shape[1], m.span()[1]+1)

        is_engine_part = np.any(special_symbol_map[row_low:row_high, col_low:col_high])

        if is_engine_part:
            engine_sum += int(m.group())

        gear_map_part = gear_map[row_low:row_high, col_low:col_high]
        gear_row, gear_col = np.nonzero(gear_map_part)
        if len(gear_row) == 1:
            row_index = row_low + gear_row
            col_index = col_low + gear_col

            gear_count[row_index, col_index] += 1
            gear_number[row_index, col_index] *= int(m.group())

print(engine_sum)
print(sum(gear_number[gear_count == 2]))
