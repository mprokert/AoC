import sys

data = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""

from collections import Counter
from util import CharGrid

cg = CharGrid(data)

start = cg.find("S")[0]
end = cg.find("E")[0]

cg.set_weights({"#": sys.maxsize})

fg = cg.dijkstra(start)

mazecost = fg[end]

total = 0
saves = Counter()

walls = cg.find("#")

for i, wall in enumerate(walls):
    r = fg.get(wall+1, sys.maxsize)
    l = fg.get(wall-1, sys.maxsize)
    u = fg.get(wall-1j, sys.maxsize)
    d = fg.get(wall+1j, sys.maxsize)
    if l <= mazecost and r <= mazecost:
            saved = abs(r-l) -2
            if saved >= 100:
                total += 1
            saves[saved] += 1

    if u <= mazecost and d <= mazecost:
            saved = abs(u-d) -2
            if saved >= 100:
                total += 1
            saves[saved] += 1

print(total)
cheats = {}
saves = Counter()

for pos in fg:
    start_val = fg.get(pos, sys.maxsize)
    if start_val < sys.maxsize:
        for i in range(-20, 21):
            for j in range(-20 + abs(i), 21-abs(i)):
                if i == j == 0:
                    continue
                end_val = fg.get(complex(i, j)+pos, sys.maxsize)
                if end_val < sys.maxsize:
                    if start_val < end_val:
                        cheats[start_val, end_val] = abs(start_val - end_val) - abs(j) - abs(i)
                    else:
                        cheats[end_val, start_val] = abs(start_val - end_val) - abs(j) - abs(i)

total = 0
for cheat in cheats.values():
    saves[cheat] += 1
    if cheat >= 100:
        total += 1

print(total)
