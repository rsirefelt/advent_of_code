def calc(lines):
  accu = line_idx = 0
  visited_idxs = {}
  while line_idx not in visited_idxs:
    visited_idxs[line_idx] = line_idx
    cmd, val = lines[line_idx].split()
    if cmd == 'nop':
      line_idx += 1
    elif cmd == 'acc':
      accu += int(val)
      line_idx += 1
    else:
      line_idx += int(val)

    if line_idx == len(lines):
      return accu, line_idx

  return accu, line_idx


with open("input.txt") as f:
  lines = f.read().splitlines()

lines = {idx: line for idx, line in enumerate(lines)}

# Part1
print(calc(lines))

# Part2
for idx, line in lines.items():
  cmd, val = line.split()
  if cmd == 'nop':
    lines[idx] = line.replace("nop", "jmp")
  elif cmd == 'jmp':
    lines[idx] = line.replace("jmp", "nop")

  accu, line_idx = calc(lines)
  lines[idx] = line
  if line_idx == len(lines):
    print(accu)
    break
