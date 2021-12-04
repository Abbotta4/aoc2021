with open("input.txt", 'r') as f:
    boards = f.read().split('\n\n')
draws, boards = boards[0].split(','), boards[1:]

def find_earliest_bingo(board):
    earliest_bingo = len(draws)
    rows = board.split('\n')
    cols = [''] * len(rows)
    for row in rows:
        for i, number in enumerate(row.split()):
            cols[i] += number + ' '
    for bingo in rows + cols:
        drawn = []
        for number in bingo.split():
            if number not in draws:
                break
            else:
                drawn.append(draws.index(number))
        else: # all numbers were drawn
            earliest_bingo = min(earliest_bingo, max(drawn))
    return earliest_bingo

latest = 0
latest_score = None
for board in boards:
    bingo = find_earliest_bingo(board)
    if bingo > latest:
        unmarked_sum = 0
        latest = bingo
        for number in board.split():
            if number not in draws[:bingo+1]:
                unmarked_sum += int(number)
        latest_score = unmarked_sum * int(draws[bingo])

print(latest_score)
