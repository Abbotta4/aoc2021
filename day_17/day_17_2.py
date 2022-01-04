import re, math
with open('input.txt', 'r') as f:
    target_area = f.read().strip()
target_area = [tuple(map(int, x.split('..'))) for x in re.findall(r'-?\d+\.\.-?\d+', target_area)]

def in_target_area(coord):
    if coord[0] >= target_area[0][0] and coord[0] <= target_area[0][1]:
        if coord[1] >= target_area[1][0] and coord[1] <= target_area[1][1]:
            return True
    return False


min_xv = int(math.ceil((math.sqrt(1 + 8 * target_area[0][0]) - 1) / 2))
max_xv = target_area[0][1]
min_yv = target_area[1][0]
max_yv = abs(target_area[1][0]) - 1

apex = max_yv*((max_yv-1)/2 + 1)

valid_coords = 0

for x in range(min_xv, max_xv+1):
    for y in range(min_yv, max_yv+1):
        step, x0, y0 = 0, 0, 0
        while True:
            x0 += max(x - step, 0)
            y0 += y - step
            step += 1
            if in_target_area((x0, y0)):
                valid_coords += 1
                break
            if y0 < target_area[1][0] or x0 > target_area[0][1]:
                break
            
print(valid_coords)
