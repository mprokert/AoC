data = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

grid = {}
regions = []

for y, line in enumerate(data.splitlines()):
    for x, ch in enumerate(line):
        grid[(x, y)] = ch

backup = grid.copy()

def find_region(g, pos, ch, region):
    x, y = pos
    for cpos in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if g.get(cpos) == ch:
            region.append(cpos)
            g.pop(cpos)
            region = find_region(g, cpos, ch, region)
    return region

while grid:
    pos, ch = grid.popitem()
    region = [pos]
    region = find_region(grid, pos, ch, region)
    regions.append(region)


def find_region(g, pos, ch, region):
    x, y = pos
    for cpos in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if g.get(cpos) == ch:
            region.append(cpos)
            g.pop(cpos)
            region = find_region(g, cpos, ch, region)
    return region

def get_neighbors(pos):
    nb = {}
    x, y = pos
    for cpos, di in [((x - 1, y), "w"), ((x + 1, y), "e"), ((x, y - 1), "n"), ((x, y + 1), "s")]:
        if cpos in backup:
            nb[cpos] = di
    return nb

def calc_umf(region):
    umf = 0
    for pos in sorted(region):
        p_umf = 4
        nb = get_neighbors(pos)
        for n in nb:
            if n in region:
                p_umf -= 1
        umf += p_umf
    return umf

def get_fences(region):
    fences = []
    for pos in region:
        dirs = {"n", "e", "s", "w"}
        nb = get_neighbors(pos)
        for n, di in nb.items():
            if n in region:
                dirs.remove(di)

        for di in list(dirs):
            fences.append((pos, di))
    return fences

def get_sides(fences):
    sides = 0
    while fences:
        pos, di = fences.pop()
        sides += 1
        x, y = pos
        if di in "ns":
            while ((x+1, y), di) in fences[:]:
                fences.remove(((x+1, y), di))
                x += 1

            x, y = pos
            while ((x-1, y), di) in fences[:]:
                fences.remove(((x-1, y), di))
                x -= 1

        if di in "ew":
            while ((x, y+1), di) in fences[:]:
                fences.remove(((x, y+1), di))
                y += 1

            x, y = pos
            while ((x, y-1), di) in fences[:]:
                fences.remove(((x, y-1), di))
                y -= 1

    return sides


price = 0
for r in regions:
    price += len(r) * calc_umf(r)

print(price)

p2 = 0
for r in regions:
    fences = get_fences(r)
    sides = get_sides(fences)
    p2 += len(r) * sides
print(p2)
