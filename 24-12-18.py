import sys

data = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

size = 7
blocks = 12

bytelist = []
for line in data.splitlines():
    x, y = line.split(",")
    bytelist.append(complex(int(x), int(y)))

from util import CharGrid

cg = CharGrid(size * (size * "." + "\n"))
for i in range(blocks):
    cg.grid[bytelist[i]] = "#"

cg.set_weights({"#": sys.maxsize})
final_grid = cg.dijkstra()

print(final_grid[complex(cg.nrows-1, cg.ncolumns-1)])

g = cg.grid.copy()


cg = CharGrid(size * (size * "." + "\n"))
for i in range(blocks):
    cg.grid[bytelist[i]] = "#"


mini = blocks
maxi = len(bytelist)

while maxi-mini > 1:
    next_ = (maxi+mini) // 2

    cg.grid = g.copy()

    for i in range(blocks, next_+1):
        cg.grid[bytelist[i]] = "#"
    cg.set_weights({"#": sys.maxsize})
    sp = cg.dijkstra()
    if sp[complex(cg.nrows - 1, cg.ncolumns - 1)] == sys.maxsize:
        maxi = next_
    else:
        mini = next_

print(f"{int(bytelist[maxi].real)},{int(bytelist[maxi].imag)}")
