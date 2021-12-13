with open('input.txt', 'r') as f:
    dots = f.read()
dots, folds = dots.split('\n\n')

dots = set([(int(x), int(y)) for x, y in map(lambda l: l.split(','), dots.split('\n'))])
folds = [(axis[-1], int(line)) for axis, line in map(lambda l: l.split('='), folds.strip().split('\n'))]

fold = folds[0][1]
for dot in list(filter(lambda x: x[0] > fold, dots)).copy():
    try:
        dots.add((2*fold - dot[0], dot[1]))
    except IndexError:
        pass

dots = list(filter(lambda x: x[0] < fold, dots))
print(len(dots))
