fish = list(map(int, list(open("06.csv"))[0].split(',')))

fishD = {i:0 for i in range(9)}

for f in fish:
    fishD[f] += 1

days = 256
for _ in range(days):
    zeroes = fishD[0]
    for i in range(1, 9):
        fishD[i-1] = fishD[i]
    fishD[6] += zeroes
    fishD[8] = zeroes

print(sum(list(fishD.values())))
