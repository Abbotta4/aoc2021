import heapq

with open('input.txt') as f:
    risk_levels = f.read()
max_x = len(risk_levels.split('\n')[0].strip())
max_y = len(risk_levels.strip().split('\n'))
risk_levels = {
    complex(r, c): int(col)
    for r, row in enumerate(risk_levels.strip().split('\n'))
    for c, col in enumerate(row)
}

for r in range(5):
    for c in range(5):
        if r == 0 and c == 0:
            continue
        for row in range(max_y):
            for col in range(max_x):
                risk_levels[complex(row+max_y*r, col+max_x*c)] = risk_levels[complex(row, col)] + r + c
                if risk_levels[complex(row+max_y*r, col+max_x*c)] > 9:
                    risk_levels[complex(row+max_y*r, col+max_x*c)] -= 9

# need this class because complex numbers can't be compared
# with the < operator, which will happen when the tuples are
# compared in heapq.heappush below
class AlwaysLess:
    def __lt__(self, other):
        return True

node_costs = [(0, AlwaysLess(), complex(0, 0))] # node (0, 0) with cost 0
visited = set()

while node_costs:
    cost, _, node = heapq.heappop(node_costs)
    if node == complex(max_x*5-1, max_y*5-1):
        print(cost)
        break
    for offset in complex(1, 0), complex(0, 1), complex(-1, 0), complex(0, -1):
        adjacent = node + offset
        if adjacent in risk_levels and adjacent not in visited:
            heapq.heappush(node_costs, (cost + risk_levels[adjacent], AlwaysLess(), adjacent))
            visited.add(adjacent)
