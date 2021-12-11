from itertools import product

with open("input.txt", 'r') as f:
    octopuses = f.read()

octopuses = {
    complex(r, c): int(col)
    for r, row in enumerate(octopuses.strip().split('\n'))
    for c, col in enumerate(row)
}

flashes = 0
for day in range(100):
    for i in octopuses:
        octopuses[i] += 1

    while True:
        for i in octopuses:
            if octopuses[i] > 9:
                for offset in product((-1, 0, 1), repeat=2):
                    adj = i + complex(*offset)
                    if adj in octopuses:
                        octopuses[adj] += 1 if octopuses[adj] != 0 else 0
                octopuses[i] = 0
                flashes += 1
                break
        else:
            break

print(flashes)
