import csv

# create a bingo num flyweight --> we don't have to update every board
b = {i:[False, i] for i in range(0,100)}

boards = []
with open("04.csv") as f:
    reader = csv.reader(f)
    draw = list(map(int, next(reader)))
    next(reader)
    board = []
    for row in reader:
        if len(row) < 1:
            boards.append(board[:] + list(map(list, list(zip(*board)))))
            board = []
        else:
            board.append([b[int(i)] for i in filter(None,row[0].split(" "))])

for d in draw:
    line = []
    b[d][0] = True
    for i,brd in enumerate(boards):
        for line in brd:
            if all([x[0] for x in line]):
                ans = [x[1] for x in line]
                s = 0
                for row in brd[:5]:
                    for v in row:
                        s += v[1] if not v[0] else 0
                print(f"board {i} wins | {ans} | {s*d}")
                break
        else:
            continue
        break
    else:
        continue
    break