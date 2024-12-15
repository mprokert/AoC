from util import CharGrid
data = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

g, m = data.split("\n\n")

cg = CharGrid(g)
moves = []

for move in m:
    if move == "^":
        moves.append(-1j)
    elif move == "v":
        moves.append(1j)
    elif move == "<":
        moves.append(-1)
    elif move == ">":
        moves.append(1)

robot = cg.find("@")[0]

for m in moves:
    positions, chars = cg.get_items(robot, m)
    j = chars.index("#")
    try:
        i = chars.index(".")
    except ValueError:
        continue
    if j < i:
        continue
    cg.grid[robot] = "."
    robot += m
    cg.grid[robot] = "@"
    if robot != positions[i]:
        cg.grid[positions[i]] = "O"

boxes = cg.find("O")

total = 0

for box in boxes:
    total += 100*box.imag
    total += box.real

print(int(total))

g = g.replace(".", "..").replace("#", "##").replace("@", "@.").replace("O", "[]")
bcg = CharGrid(g)
robot = bcg.find("@")[0]

def move(start, direction, check=False):
    positions, chars = bcg.get_items(start, direction)
    j = chars.index("#")
    try:
        i = chars.index(".")
    except ValueError:
        return False
    if j < i:
        return False
    if direction in (1, -1):
        if check:
            return True
        for j in range(i, 0, -1):
            bcg.grid[positions[j]] = chars[j-1]
        bcg.grid[start] = "."
        return True
    else:
        if check:
            if chars[1] == "#":
                return False
            if chars[1] == ".":
                return True
            if chars[1] == "[":
                return move(positions[1], direction, check) and move(positions[1] + 1, direction, check)
            if chars[1] == "]":
                return move(positions[1], direction, check) and move(positions[1] - 1, direction, check)
        else:
            if chars[1] == "[":
                move(positions[1], direction, check)
                move(positions[1] + 1, direction, check)
            elif chars[1] == "]":
                move(positions[1], direction, check)
                move(positions[1] - 1, direction, check)

            positions, chars = bcg.get_items(start, direction)
            bcg.grid[positions[1]] = chars[0]
            bcg.grid[positions[0]] = chars[1]


for m in moves:
    if move(robot, m, True):
        move(robot, m, False)
        robot += m

print(bcg)

total = 0
boxes = bcg.find("[")
for box in boxes:
    total += 100*box.imag
    total += box.real

print(int(total))
