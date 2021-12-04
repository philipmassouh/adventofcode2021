import csv

def read_csv(filename):
    with open(filename, "rt") as csv_in:
        for row in csv.reader(csv_in):
            out = row[0].split(' ')
            out[1] = int(out[1])
            yield out

horiz = 0
depth = 0
aim = 0
for r in read_csv("02.csv"):
    direction = r[0]
    distance = r[1]

    if direction == "down":
        aim += distance
    elif direction == "up":
        aim -= distance
    elif direction == "forward":
        horiz += distance
        depth += aim*distance


print(horiz*depth)