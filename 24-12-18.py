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

cg.grid2 = cg.grid.copy()
for k in cg.grid2:
    cg.grid2[k] = 99999
cg.grid2[0+0j] = 0

changed = True
while changed:
    changed = False
    for pos in cg.grid.keys():
        if cg.grid2[pos] < 99999:
            shortest = cg.grid2[pos] + 1
            for nb in cg.get_neighbors(pos):
                if cg.grid[nb] == "." and cg.grid2[nb] > shortest:
                    cg.grid2[nb] = shortest
                    changed = True
print(cg.grid2[complex(cg.nrows-1, cg.ncolumns-1)])


cg = CharGrid(size * (size * "." + "\n"))
for i in range(blocks):
    cg.grid[bytelist[i]] = "#"

cg.grid2 = cg.grid.copy()
for k in cg.grid2:
    cg.grid2[k] = 99999
cg.grid2[0+0j] = 0

g = cg.grid.copy()
g2 = cg.grid2.copy()

mini = blocks
maxi = len(bytelist)

while maxi-mini > 1:
    next_ = (maxi+mini) // 2

    cg.grid = g.copy()
    cg.grid2 = g2.copy()

    for i in range(blocks, next_+1):
        cg.grid[bytelist[i]] = "#"

    changed = True
    while changed:
        changed = False
        for pos in cg.grid.keys():
            if cg.grid2[pos] < 99999:
                shortest = cg.grid2[pos] + 1
                for nb in cg.get_neighbors(pos):
                    if cg.grid[nb] == "." and cg.grid2[nb] > shortest:
                        cg.grid2[nb] = shortest
                        changed = True

    if cg.grid2[complex(cg.nrows - 1, cg.ncolumns - 1)] == 99999:
        maxi = next_
    else:
        mini = next_

print(f"{int(bytelist[maxi].real)},{int(bytelist[maxi].imag)}")
