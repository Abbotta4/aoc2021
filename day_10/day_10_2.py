import re

with open("input.txt", 'r') as f:
    lines = f.readlines()

scores = list()
for line in lines:
    score = 0
    chunks = ('()', '[]', '{}', '<>')
    while True:
        for chunk in chunks:
            line, subs = re.subn(re.escape(chunk), '', line)
            if subs != 0:
                break
        else:
            break

    # skip invalid lines
    if any(x in (')', ']', '}', '>') for x in line):
        continue

    for character in line.strip()[::-1]:
        score *= 5
        if character == '(':
            score += 1
        elif character == '[':
            score += 2
        elif character == '{':
            score += 3
        elif character == '<':
            score += 4

    scores.append(score)

print(sorted(scores)[len(scores)//2])
