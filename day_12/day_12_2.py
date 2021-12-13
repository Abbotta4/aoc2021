with open('input.txt', 'r') as f:
    connections = f.readlines()
connections = [tuple(sorted(x.strip().split('-'))) for x in connections]
caves = set()
for c1, c2 in connections:
    caves.add(c1)
    caves.add(c2)

next_caves = dict()

def generate_next_caves(caves):
    for cave in caves:
        next_caves[cave] = list()
        for connection in connections:
            if cave == connection[0]:
                for freq in range(caves.count(connection[1])):
                    next_caves[cave].append(connection[1])
            elif cave == connection[1]:
                for freq in range(caves.count(connection[0])):
                    next_caves[cave].append(connection[0])
                
def find_paths(start, path, caves):
    if start == 'end':
        yield path + [start]
    for cave in next_caves[start]:
        if path.count(cave) < caves.count(cave) or cave.isupper():
            yield from find_paths(cave, path + [start], caves)

total_paths = set()
for cave in filter(lambda x: x.islower() and len(x) <= 2, caves):
    _caves = list(caves) + [cave]
    generate_next_caves(_caves)
    for path in find_paths('start', list(), _caves):
        total_paths.add(','.join(path))

print(len(total_paths))
