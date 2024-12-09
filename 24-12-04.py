data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

array = []
for line in data.splitlines():
    array.append([c for c in line])

total = 0

for line in array:
    for i in range(len(line)-3):
        if "".join(line[i:i+4]) in ("XMAS", "SAMX"):
            total += 1

print(f"w {total}")

transposed = []
for x in range(len(array[0])):
    tmp = []
    for y in range(len(array)):
        tmp.append(array[y][x])
    transposed.append(tmp[:])

for line in transposed:
    for i in range(len(line)-3):
        if "".join(line[i:i+4]) in ("XMAS", "SAMX"):
            total += 1

print(f"s {total}")

moved = []
for y in range(len(array)):
    tmp = y * ["."]
    for x in range(len(array[0])):
        tmp.append(array[y][x])
    while len(tmp) < 2*len(array[0])-1:
        tmp.append(".")
    moved.append(tmp)

transposed = []
for x in range(len(moved[0])):
    tmp = []
    for y in range(len(moved)):
        tmp.append(moved[y][x])
    transposed.append(tmp)

for line in transposed:
    for i in range(len(line)-3):
        if "".join(line[i:i+4]) in ("XMAS", "SAMX"):
            total += 1

print(f"d1 {total}")

moved = []
for y in range(len(array)):
    tmp = (len(array[0])- 1 - y) * ["."]
    for x in range(len(array[0])):
        tmp.append(array[y][x])
    while len(tmp) < 2*len(array[0])-1:
        tmp.append(".")
    moved.append(tmp)

transposed = []
for x in range(len(moved[0])):
    tmp = []
    for y in range(len(moved)):
        tmp.append(moved[y][x])
    transposed.append(tmp)

for line in transposed:
    for i in range(len(line)-3):
        if "".join(line[i:i+4]) in ("XMAS", "SAMX"):
            total += 1

print(f"d2 {total}")

total2 = 0

import re

rexs = [re.compile(x) for x in ["M.S.A.M.S", "M.M.A.S.S", "S.S.A.M.M", "S.M.A.S.M"]]

for y in range(len(array)-2):
    for x in range(len(array[0])-2):
        s = array[y][x] + array[y+1][x] + array[y+2][x]
        s += array[y][x+1] + array[y + 1][x+1] + array[y + 2][x+1]
        s += array[y][x+2] + array[y + 1][x+2] + array[y + 2][x+2]
        for rex in rexs:
            if rex.match(s):
                total2 += 1
                break

print(total2)
