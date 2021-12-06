import re

with open("input.txt", 'r') as f:
    lines = f.readlines()
lines = tuple(map(lambda x: re.search("(\d+),(\d+) -> (\d+),(\d+)", x).group(1, 2, 3, 4), lines))
lines = tuple(map(lambda x: tuple(map(int, x)), lines))

coords = set()
overlaps = set()
for line in lines:
    if line[0] == line[2]:
        loop_list = list(range(line[1], line[3], 1 if line[3] > line[1] else -1))
        loop_list.append(line[3])
    elif line [1] == line[3]:
        loop_list = list(range(line[0], line[2], 1 if line[2] > line[0] else -1))
        loop_list.append(line[2])
    else:
        continue
    for var in loop_list:
        coord = (line[0], var) if line[0] == line[2] else (var, line[1])
        if coord in coords:
            overlaps.add(coord)
        coords.add(coord)

print(len(overlaps))
