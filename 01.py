import csv

def read_csv(filename):
    with open(filename, "rt") as csv_in:
        for row in csv.reader(csv_in):
            yield int(row[0])

last_val = -1
increases = -1
for i,val in enumerate(read_csv("01.csv")):
    if last_val < val:
        increases += 1
    last_val = val

print(increases)
