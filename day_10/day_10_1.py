import re

with open("input.txt", 'r') as f:
    lines = f.readlines()

score = 0
for line in lines:
    chunks = ('()', '[]', '{}', '<>')
    while True:
        for chunk in chunks:
            line, subs = re.subn(re.escape(chunk), '', line)
            if subs != 0:
                break
        else:
            break

    for character in line:
        if character == ')':
            score += 3
            break
        if character == ']':
            score += 57
            break
        if character == '}':
            score += 1197
            break
        if character == '>':
            score += 25137
            break

print(score)
