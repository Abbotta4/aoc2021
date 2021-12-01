with open("input.txt", 'r') as f:
    depths = f.read().splitlines()
    depths = list(map(int, depths))

prev, larger = float('inf'), 0
for depth in depths:
    if depth > prev:
        larger += 1
    prev = depth

print(larger)
