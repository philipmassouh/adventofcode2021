from collections import namedtuple
import re

class Canvas:

    def __init__(self, x, y):
        self.canvas = [[0 for _ in range(x+1)] for _ in range(y+1)]

    def __str__(self):
        s = ''
        for line in self.canvas:
            s += "".join(list(map(lambda x: '.' if x==0 else str(x), line)))+'\n'
        return s

    def drawX(self, y, x1, x2):
        for x in range(x1, x2+1):
            self.canvas[y][x] += 1

    def drawY(self, x, y1, y2):
        for y in range(y1, y2+1):
            self.canvas[y][x] += 1
        

    #todo typehints namedtuple?
    def draw(self, vector):
        if vector.x1 == vector.x2:
            y_ord = sorted([vector.y1, vector.y2])
            self.drawY(vector.x1, y_ord[0], y_ord[1])
        elif vector.y1 == vector.y2:
            x_ord = sorted([vector.x1, vector.x2])
            self.drawX(vector.y1, x_ord[0], x_ord[1])
        else:
            pass

    def get_intersections(self):
        a = 0
        for row in self.canvas:
            for v in row:
                if v > 1:
                    a += 1
        return a

Vector = namedtuple('vector', 'x1 y1 x2 y2')
bds = [0,0]
vectors = []
with open("05.csv") as f:
    for x in f:
        v = list(map(int, re.findall(r'\d+', x)))
        bds[0] = bds[0] if bds[0] > max(v[:2]) else max(v[:2])
        bds[1] = bds[1] if bds[1] > max(v[2:]) else max(v[2:])
        vectors.append(Vector(*v))

c = Canvas(1000, 1000)
print(bds)

for v in vectors:
    c.draw(v)

# print(c)
print(c.get_intersections())

        