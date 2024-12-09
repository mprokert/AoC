data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


obstacles = set()

directions = {
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
}

lines = data.splitlines()
YMAX = len(lines) - 1
XMAX = len(lines[0]) - 1

for y, line in enumerate(lines):
    for x, ch in enumerate(line):
        if ch == "^":
            start_pos = (x, y, (0, -1))
        elif ch == "#":
            obstacles.add((x, y))

def step(pos, obstacles, seen, seen_direction):
    x, y, direction = pos
    dx, dy = direction
    xn, yn = x + dx, y + dy
    if not 0 <= xn <= XMAX:
        seen.add((x, y))
        return x, y, (0, 0)  # free
    if not 0 <= yn <= YMAX:
        seen.add((x, y))
        return x, y, (0, 0)  # free
    if (xn, yn) in obstacles:
        return x, y, directions[direction]

    seen.add((x, y))
    if not (x, y, direction) in seen_direction:
        seen_direction.add((x, y, direction))
    else:
        return x, y, (1, 1)  # loop
    return xn, yn, direction

pos = start_pos
seen = set()
seen_direction = set()

while True:
    pos = step(pos, obstacles, seen, seen_direction)
    if pos[2] == (0, 0):
        print(len(seen))
        break

total = 0
while seen:
    new_obs = seen.pop()
    new_obstacles = obstacles.copy()
    new_obstacles.add(new_obs)

    pos = start_pos
    seen_new = set()
    seen_direction = set()

    while True:
        pos = step(pos, new_obstacles, seen_new, seen_direction)
        if pos[2] == (0, 0):
            break
        elif pos[2] == (1, 1):
            total += 1
            break

print(total)
