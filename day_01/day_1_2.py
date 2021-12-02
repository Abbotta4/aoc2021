with open("input.txt", 'r') as f:
    depths = f.read().splitlines()
    depths = list(map(int, depths))

prev, larger = float('inf'), 0
for a, b, c in zip(depths, depths[1:], depths[2:]):
    window_sum = a + b + c
    if window_sum > prev:
        larger += 1
    prev = window_sum

print(larger)
