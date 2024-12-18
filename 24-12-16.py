data = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""

from util import CharGrid

cg = CharGrid(data)

start = cg.find("S")[0]
path = (start,)

direction = 1

checked = {}
m_cost = 99999999
steps = [(start, path, direction)]
best_path = []

def step(pos, path, direction):
    global m_cost, visitor_set
    c = cost(path)
    if c > m_cost:
        return

    if cg[pos+direction] == "E":
        if c == m_cost:
            best_path.extend(path)
        if c < m_cost:
            best_path.clear()
            best_path.extend(path)
            m_cost = c
        return

    if cg[pos+direction] == "." and pos+direction not in path:
        k = (pos+direction, direction)
        if k in checked and checked[k] < c:
            pass
        else:
            checked[k] = c
            steps.append((pos+direction, path + (pos+direction,), direction))

    for new_dir in [direction * r for r in [1j,-1j]]:
        if cg[pos+new_dir] != "#" and cg[pos+new_dir] not in path:
            if path[-1] == "t":
                continue
            steps.append((pos, path + ("t",), new_dir))

def cost(path):
    cost = 0
    for s in path:
        if s == "t":
            cost += 1000
        else:
            cost += 1
    return cost

while steps:
    step_ = steps.pop(0)
    step(*step_)

print(m_cost)
print(len(set([p for p in best_path if p!="t"])) + 1)
