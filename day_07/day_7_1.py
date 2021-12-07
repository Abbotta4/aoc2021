with open("input.txt", 'r') as f:
    crabs = f.readline().split(',')
crabs = list(map(int, crabs))

fuel_cost = []
for position in range(max(crabs)+1):
    fuel = 0
    for crab in crabs:
        fuel += abs(position - crab)
    fuel_cost.append(fuel)

print(min(fuel_cost))
