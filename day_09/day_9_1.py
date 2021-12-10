with open("input.txt", 'r') as f:
    rows = f.readlines()

def find_adjacents(rows, row, col):
    adjacents = list()
    row_len = len('{}'.format(rows[row].strip()))
    if row-1 >= 0:
        adjacents.append(rows[row-1][col])
    if row+1 <= len(rows)-1:
        adjacents.append(rows[row+1][col])
    if col-1 >= 0:
        adjacents.append(rows[row][col-1])
    if col+1 <= row_len-1:
        adjacents.append(rows[row][col+1])
    return adjacents

def check_low_point(rows, row, col):
    adjacents = find_adjacents(rows, row, col)
    for point in adjacents:
        if point <= rows[row][col]:
            return False
    return True

risk_level_total = 0
for row in range(len(rows)):
    _row = rows[row].strip()
    for col in range(len(_row)):
        if check_low_point(rows, row, col):
            risk_level_total += int(rows[row][col]) + 1

print(risk_level_total)
