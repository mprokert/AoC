import itertools

data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

grid = {}
ants = {}
antinodes = set()

for y, line in enumerate(data.splitlines()):
    for x, ch in enumerate(line):
        grid[complex(x,y)] = ch
        if ch != ".":
            ants.setdefault(ch, []).append(complex(x,y))

for k in ants:
    for loc1, loc2 in itertools.combinations(ants[k], 2):
        d = loc1 - loc2
        a1 = loc1 + d
        if a1 in grid:
            antinodes.add(a1)

        a2 = loc2-d
        if a2 in grid:
            antinodes.add(a2)

print(len(antinodes))

for k in ants:
    for loc1, loc2 in itertools.combinations(ants[k], 2):
        antinodes.add(loc1)
        antinodes.add(loc2)
        d = loc1 - loc2
        a1 = loc1 + d
        while a1 in grid:
            antinodes.add(a1)
            a1 += d

        a2 = loc2 - d
        while a2 in grid:
            antinodes.add(a2)
            a2 -= d

print(len(antinodes))
