data = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

SIZEX = 11
SIZEY = 7

import re
from collections import Counter

bots = {}

for i, bot in enumerate(re.findall(r"p=(\d+),(\d+) v=([-\d]+),([-\d]+)", data)):
    bots[i] = [int(x) for x in bot]

def move(bot):
    new_x = bot[0] + bot[2]
    new_y = bot[1] + bot[3]

    if new_x < 0:
        new_x += SIZEX
    if new_x >= SIZEX:
        new_x -= SIZEX
    if new_y < 0:
        new_y += SIZEY
    if new_y >= SIZEY:
        new_y -= SIZEY
    return new_x, new_y, bot[2], bot[3]

smallest = 1234567890

for step in range(1, 12345):
    grid = Counter()
    for i, bot in bots.items():
        x, y, vx, vy = move(bot)
        bots[i] = x, y, vx, vy
        grid[(x, y)] += 1

    if step == 100:
        gnw = 0
        gne = 0
        gsw = 0
        gse = 0

        for bot in bots.values():
            x, y, _, _ = bot
            if 0 <= x < SIZEX // 2 and 0 <= y < SIZEY // 2:
                gnw += 1

            if 0 <= x < SIZEX // 2 and SIZEY // 2 < y < SIZEY:
                gsw += 1

            if SIZEX // 2 < x < SIZEX and 0 <= y < SIZEY // 2:
                gne += 1

            if SIZEX // 2 < x < SIZEX and SIZEY // 2 < y < SIZEY:
                gse += 1

        print(gse * gnw * gsw * gne)

    dist = 0
    for (x, y) in grid:
        dist += abs(y-SIZEY/2)+abs(x-SIZEX/2)

    if dist < smallest:
        smallest = dist
        smallest_grid = grid
        smallest_step = step

print(smallest_step)
for y in range(SIZEY):
    s = ""
    for x in range(SIZEX):
        if (x, y) in smallest_grid:
            s+= str(smallest_grid[(x, y)])
        else:
            s += "."
    print(s)
