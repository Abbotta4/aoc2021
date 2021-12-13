with open('input.txt', 'r') as f:
    connections = f.readlines()
connections = [tuple(sorted(x.strip().split('-'))) for x in connections]
caves = set()
for c1, c2 in connections:
    caves.add(c1)
    caves.add(c2)

next_caves = dict()
for cave in caves:
    next_caves[cave] = list()
    for connection in connections:
        if cave in connection:
            next_caves[cave].append(connection[0 if connection[1] == cave else 1])

def find_paths(start, path):
    if start == 'end':
        yield path + [start]
    for cave in next_caves[start]:
        if not cave in path or cave.isupper():
            yield from find_paths(cave, path + [start])

print(len([path for path in find_paths('start', list())]))
