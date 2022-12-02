with open("input") as f:
    input = f.readlines()

elves = []
index = 0
elves.append(0)
for line in input:
    if line == "" or line == "\n":
        index += 1
        elves.append(0)
    else:
        elves[index] += int(line)

sorted_elves = sorted(elves, reverse=True)
print("top: " + str(sorted_elves[0]))
print("top 3: " + str(sorted_elves[0] + sorted_elves[1] + sorted_elves[2]))