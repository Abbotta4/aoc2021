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

for step in range(10):
    old_polymer = polymer
    polymer = ''
    for pair in pairwise(old_polymer):
        polymer += pair[0] + pair_insertions[''.join(pair)]
    polymer += old_polymer[-1]

elements = set()
for element in polymer:
    elements.add(element)

quantities = [polymer.count(element) for element in elements]
quantities.sort()

print(quantities[-1] - quantities[0])
