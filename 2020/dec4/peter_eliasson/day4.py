import re

with open("regex.txt") as f:
	regex = re.compile(f.read())
with open("input.txt") as f:
    print(len(regex.findall(f.read())))
