import re
with open('input.txt', 'r') as f:
    target_area = f.read().strip()
target_area = [tuple(map(int, x.split('..'))) for x in re.findall(r'-?\d+\.\.-?\d+', target_area)]

# prove will always return to 0 and then move velocity+1 downward from there
max_yv = abs(target_area[1][0]) - 1
# sum of (n-1)+(n-2)+...+2+1 = n*(n-1)/2
apex = int(max_yv*((max_yv-1)/2 + 1))

print(apex)
