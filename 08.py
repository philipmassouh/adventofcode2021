with open("08.csv") as f:
    c = 0
    for l in f:
        x,y = l.strip().split(" | ")
        temp = list(map(len, y.split(' ')))
        c += temp.count(2)
        c += temp.count(3)
        c += temp.count(4)
        c += temp.count(7)

print(c)



