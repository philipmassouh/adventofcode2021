def a(x):
    two = set(list(filter(lambda i: len(i)==2, x))[0])
    three = set(list(filter(lambda i: len(i)==3, x))[0])
    ans = next(iter(three-two))
    print(f"{ans} -> a")
    return ans

def fc(x):
    two = set(list(filter(lambda i: len(i)==2, x))[0])
    sixes = list(filter(lambda i: len(i)==6, x))
    for i,six in enumerate(sixes):
        if len(set(six).intersection(two)) == 1:
            break
    ans1 = next(iter(set(six).intersection(two)))
    ans2 = next(iter(two-{ans1}))
    print(f"{ans1} -> f")
    print(f"{ans2} -> c")
    return ans1,ans2

def bd(x):
    two = set(list(filter(lambda i: len(i)==2, x))[0])
    four = set(list(filter(lambda i: len(i)==4, x))[0])
    four -= two
    sixes = list(filter(lambda i: len(i)==6, x))
    for i,six in enumerate(sixes):
        if len(set(six).intersection(four)) == 1:
            break
    ans1 = next(iter(set(six).intersection(four)))
    ans2 = next(iter(four-{ans1}))
    print(f"{ans1} -> b")
    print(f"{ans2} -> d")
    return ans1,ans2

def ge(x):
    known = "d b a e f".split(" ")
    fives = list(filter(lambda i: len(i)==6, x))
    for five in fives:
        not_in = []
        for c in five:
            if c not in known:
                not_in.append(c)
        if len(not_in) == 1:
            ans1 = not_in[0]
    eight = set(list(filter(lambda i: len(i)==7, x))[0])
    known.append(ans1)
    ans2 = next(iter(eight - set(known)))
    print(f"{ans1} -> g")
    print(f"{ans2} -> e")
    return ans1,ans2

lookup = {
    "abcefg":0,
    "cf":1,
    "acdeg":2,
    "acdfg":3,
    "bcdf":4,
    "abdfg":5,
    "abdefg":6,
    "acf":7,
    "abcdefg":8,
    "abcdfg":9,
}

with open("08b.csv") as f:
    for l in f:
        g,output = l.strip().split(" | ")
        g = g.split(" ")
        output = output.split(" ")
        dec = {
            a(g):"a",
            fc(g)[0]:"f",
            fc(g)[1]:"c",
            bd(g)[0]:"b",
            bd(g)[1]:"d",
            ge(g)[0]:"g",
            ge(g)[1]:"e",
        }
        print(dec)
        answer = []
        for o in output:
            num = set([dec[c] for c in o])
            for key in lookup.keys():
                if set(key) == num:
                    answer.append(str(lookup[key]))
        print(answer)
