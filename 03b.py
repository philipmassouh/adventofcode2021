import csv

# read in
values_base = []
with open("03.csv", "rt") as csv_in:
    for row in csv.reader(csv_in):
        values_base.append(list(map(int, list(row[0]))))

# use this for debugging -- just rename the variable to switch between :)
values_base2 = [
    [0,0,1,0,0],
    [1,1,1,1,0],
    [1,0,1,1,0],
    [1,0,1,1,1],
    [1,0,1,0,1],
    [0,1,1,1,1],
    [0,0,1,1,1],
    [1,1,1,0,0],
    [1,0,0,0,0],
    [1,1,0,0,1],
    [0,0,0,1,0],
    [0,1,0,1,0],
]

# transpose matrix
values = list(map(list, list(zip(*values_base))))

# iterate by column
for column in values:
    # stop if you only have one answer
    if len(values[0]) < 2:
        break 
    # find value that occurs the most per column
    most_common = int(column.count(1) >= column.count(0))
    # deletion in this loop -> iterate backwards to maintain idx integrity
    for i in range(len(column)-1, -1, -1):
        # if the value in the column doesn't match
        if column[i] != most_common:
            # iterate through all columns deleting just that index
            for col in values:
                del col[i]

# we should be left with an list of singleton? lists
# unpack element -> cast to string -> add to list -> join list -> cast to int_2 
oxy = int("".join([str(v[0]) for v in values]), 2)



# we repeat the exact same process with only one change:
# most_common = int(column.count(1) 
#                                       (>=) --> (<) 
#                                                       column.count(0))
values = list(map(list, list(zip(*values_base))))
for column in values:
    if len(values[0]) < 2:
        break 
    most_common = int(column.count(1) < column.count(0))
    # print(f"{most_common} most common | ", end='')
    for i in range(len(column)-1, -1, -1):
        if column[i] != most_common:
            for col in values:
                del col[i]

co2 = int("".join([str(v[0]) for v in values]), 2)


# answer
print(oxy*co2)