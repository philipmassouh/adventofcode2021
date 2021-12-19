# brute force lol
pos = [16,1,2,0,4,2,7,1,2,14]
pos = list(map(int, list(open("07.csv"))[0].split(',')))
# arithmetic sequence
print(min([sum(abs(x-i)*(abs(x-i) + 1)//2 for x in pos) for i in range(max(pos))]))