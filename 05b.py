from collections import namedtuple
import re

class Canvas:

    def __init__(self, x, y):
        self.canvas = [[0 for _ in range(x+1)] for _ in range(y+1)]
        self.intersections = 0

    def drawPt(self, x, y):
        self.canvas[y][x] += 1
        if self.canvas[y][x] == 2:
            self.intersections += 1

    def draw(self, v):
        x = v.x1
        y = v.y1
        while x != v.x2 or y != v.y2:
            c.drawPt(x,y)
            x += -1 if v.x1>v.x2 else int(v.x1<v.x2)
            y += -1 if v.y1>v.y2 else int(v.y1<v.y2)
        c.drawPt(x,y)

        
Vector = namedtuple('vector', 'x1 y1 x2 y2')
c = Canvas(1000,1000)
with open("05.csv") as f:
    for x in f:
        c.draw(Vector(*list(map(int, re.findall(r'\d+', x)))))
print(c.intersections)
