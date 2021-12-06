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
        loop_list = [(line[0], x) for x in loop_list]
    elif line [1] == line[3]:
        loop_list = list(range(line[0], line[2], 1 if line[2] > line[0] else -1))
        loop_list = [(x, line[1]) for x in loop_list]
    elif abs(line[0] - line[2]) == abs(line[1] - line[3]):
        loop_list = []
        x_range = range(line[0], line[2], 1 if line[2] > line[0] else -1)
        y_range = range(line[1], line[3], 1 if line[3] > line[1] else -1)
        for x, y in zip(x_range, y_range):
            loop_list.append((x, y))
    else:
        continue
    loop_list.append((line[2], line[3]))
    for coord in loop_list:
        if coord in coords:
            overlaps.add(coord)
        coords.add(coord)

print(len(overlaps))
