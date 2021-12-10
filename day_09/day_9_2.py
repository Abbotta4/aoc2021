with open("input.txt", 'r') as f:
    rows = f.readlines()

def find_adjacents(rows, row, col):
    adjacents = list()
    row_len = len('{}'.format(rows[row].strip()))
    if row-1 >= 0:
        adjacents.append((row-1, col))
    if row+1 <= len(rows)-1:
        adjacents.append((row+1,col))
    if col-1 >= 0:
        adjacents.append((row,col-1))
    if col+1 <= row_len-1:
        adjacents.append((row,col+1))
    return adjacents

def check_low_point(rows, row, col):
    adjacents = find_adjacents(rows, row, col)
    for point in adjacents:
        if rows[point[0]][point[1]] <= rows[row][col]:
            return False
    return True

def find_basin(rows, row, col, basin):
    adjacents = find_adjacents(rows, row, col)
    for point in adjacents:
        if point not in basin:
            point_height = rows[point[0]][point[1]]
            if point_height > rows[row][col] and point_height != '9':
                basin.append(point)
                find_basin(rows, point[0], point[1], basin)
    
basins = list()
for row in range(len(rows)):
    _row = rows[row].strip()
    for col in range(len(_row)):
        if check_low_point(rows, row, col):
            basin = [(row, col)]
            find_basin(rows, row, col, basin)
            basins.append(len(basin))

basins.sort(reverse=True)

print(basins[0]*basins[1]*basins[2])
