data = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

grid = {}
heads = []

def check(elem):
    new_elems = []
    pos, h, path = elem
    x, y = pos
    if grid.get((x-1, y), -1) == h+1:
        new_elems.append(((x-1, y), h+1, (path + (pos,))))
    if grid.get((x+1, y), -1) == h+1:
        new_elems.append(((x+1, y), h+1, (path + (pos,))))
    if grid.get((x, y-1), -1) == h+1:
        new_elems.append(((x, y-1), h+1, (path + (pos,))))
    if grid.get((x, y+1), -1) == h+1:
        new_elems.append(((x, y+1), h+1, (path + (pos,))))
    return new_elems


for y, line in enumerate(data.splitlines()):
    for x, ch in enumerate(line):
        h = int(ch)
        grid[(x, y)] = h
        if not h:
            heads.append((x, y))

trails = set()
unique_trails = set()

for h in heads:
    stack = [(h, 0, ())]
    while stack:
        to_check = stack.pop()
        new_elems = check(to_check)
        for elem in new_elems:
            if elem[1] == 9:
                trails.add((h, elem[0]))
                unique_trails.add((h, elem[0], elem[2]))
            else:
                stack.append(elem)

print(len(trails))
print(len(unique_trails))
