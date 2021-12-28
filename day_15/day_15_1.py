from itertools import product

with open('input.txt') as f:
    risk_levels = f.read()
risk_levels = {
    complex(r, c): int(col)
    for r, row in enumerate(risk_levels.strip().split('\n'))
    for c, col in enumerate(row)
}

node_costs = {k: float('inf') for k in risk_levels}
node_costs[complex(0, 0)] = 0
unvisited_nodes = [coord for coord in risk_levels]
unvisited_nodes.remove(complex(0,0)) # starting coord

def get_adj_costs(coord):
    for offset in product((-1, 0, 1), repeat=2):
        if offset[0] * offset[1] != 0 or offset == [0, 0]:
            continue
        adj = coord + complex(*offset)
        if adj in node_costs:
            node_costs[adj] = min(node_costs[adj], node_costs[coord] + risk_levels[adj])

for row in range(100):
    for col in range(100):
        get_adj_costs(complex(row, col))
            
print(node_costs[complex(99, 99)])
