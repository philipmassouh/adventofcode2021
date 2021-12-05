a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# a = list(map(list, list(zip(*a))))
a = list(map(list, list(zip(*a))))
print(a)