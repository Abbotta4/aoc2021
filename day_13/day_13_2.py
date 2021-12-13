with open('input.txt', 'r') as f:
    dots = f.read()
dots, folds = dots.split('\n\n')

dots = set([(int(x), int(y)) for x, y in map(lambda l: l.split(','), dots.split('\n'))])
folds = [(axis[-1], int(line)) for axis, line in map(lambda l: l.split('='), folds.strip().split('\n'))]

for fold in folds:
    for dot in list(filter(lambda x: x[0 if fold[0] == 'x' else 1] > fold[1], dots)).copy():
        try:
            if fold[0] == 'x':
                dots.add((2*fold[1] - dot[0], dot[1]))
            else: # fold[1] == 'y'
                dots.add((dot[0], 2*fold[1] - dot[1]))
        except IndexError:
            pass

    dots = set(filter(lambda x: x[0 if fold[0] == 'x' else 1] < fold[1], dots))

for x in range(max([x[0] for x in dots])+1, 0, -1): # letters are backwards, so flip
    for y in range(max([x[1] for x in dots])+1):
        if (x, y) in dots:
            print('#', end='')
        else:
            print('.', end='')
    print('')
