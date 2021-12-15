from itertools import tee

with open('input.txt', 'r') as f:
    pair_insertions = f.readlines()
polymer, pair_insertions = pair_insertions[0].strip(), pair_insertions[2:]
pair_insertions = dict((pair.strip().split(' -> ') for pair in pair_insertions))

# included in itertools in 3.10, else need recipe
def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

pair_quant = {k: 0 for k in pair_insertions}

for pair in pairwise(polymer):
    pair_quant[''.join(pair)] += 1

for step in range(40):
    old_pair_quant = pair_quant.copy()
    for pair, element in old_pair_quant.items():
        first = pair[0] + pair_insertions[pair]
        second = pair_insertions[pair] + pair[1]
        pair_quant[first] += element
        pair_quant[second] += element
        pair_quant[pair] -= element

elements_quant = {k[0]: 0 for k in pair_quant}
for k, v in pair_quant.items():
    elements_quant[k[0]] += v
elements_quant[polymer[-1]] += 1

elements_quant_list = [v for k, v in elements_quant.items()]
print(max(elements_quant_list) - min(elements_quant_list))
