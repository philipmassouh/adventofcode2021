import csv
from operator import xor

def read_csv(filename):
    with open(filename, "rt") as csv_in:
        for row in csv.reader(csv_in):
            yield row[0]

total = [0]*12
for i,value in enumerate(read_csv("03.csv")):
    for j,v in enumerate(value):
        total[j] += int(v)

gamma = int("".join([str(int(t>i/2)) for t in total]), 2)
eps = int("".join([str(int(t<i/2)) for t in total]),2)

print(gamma)
print(eps)
print(gamma*eps)