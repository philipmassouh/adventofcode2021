import csv

#TODO make it work with a generator 
#   or just read directly into numpy array
#       nevertheless, it's fast enough

def read_csv(filename):
    lazy = []
    with open(filename, "rt") as csv_in:
        for row in csv.reader(csv_in):
            lazy.append(int(row[0]))
    return lazy

m = read_csv("001.csv")

increases = 0
for i in range(len(m) - 3):
    if sum(m[i:i+3]) < sum(m[i+1:i+4]):
        increases += 1

print(increases)