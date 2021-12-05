import csv

# create a bingo num flyweight --> we don't have to update every board
b = {i:[False] for i in range(0,100)}

boards = []
with open("04.csv") as f:
    reader = csv.reader(f)
    # get the numbers to be drawn
    draw = list(map(int, next(reader)))
    # skip the first emptyline before boards start
    next(reader)
    # we want to store each board as a list of rows and columns
    #   i.e. 5x5 board is a 5x10 list, this will make checking easier
    board = []
    for row in reader:
        print(row)
        if len(row) < 1:
            boards.append(board[:] + list(map(list, list(zip(*board)))))
            board = []
        else:
            board.append([b[int(i)] for i in filter(None,row[0].split(" "))])

def bingo(board, line):
    for l in board:
        if all([x[0] for x in board]):
            print(l)
            return True
    return False
    

for d in draw:
    line = []
    b[d][0] = True
    for brd in boards:
        if bingo(brd, line):
            print(line)
            break

# you need the value in the board as well. probably a list
