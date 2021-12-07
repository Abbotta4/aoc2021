with open("input.txt", 'r') as f:
    crabs = f.readline().split(',')
crabs = list(map(int, crabs))

memo = dict()
def calc_fuel_cost(distance):
    if distance in memo:
        return memo[distance]
    fuel = 0
    for step in range(1, distance+1):
        fuel += step
    memo[distance] = fuel
    return fuel


fuel_cost = []
for position in range(max(crabs)+1):
    fuel = 0
    for crab in crabs:
        diff = abs(position - crab)
        fuel += calc_fuel_cost(diff)
    fuel_cost.append(fuel)

print(min(fuel_cost))
