data = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

lines = data.splitlines()
towels = lines[0].split(", ")
patterns = lines[2:]

import functools
import re

unique_towels = []
for towel in sorted(towels, key=len):
    rex = re.compile(f"(^({"|".join(unique_towels)})+$)")
    if not rex.match(towel):
        unique_towels.append(towel)

rex = re.compile(f"(^({"|".join(unique_towels)})+$)")

total = 0
for pattern in patterns:
    if rex.match(pattern):
        total += 1
print(total)

@functools.cache
def matches(pattern):
    if pattern == "":
        return 1
    s = 0
    for towel in towels:
        if pattern.startswith(towel):
            s += matches(pattern[len(towel):])
    return s

total = 0
total2 = 0
for pattern in patterns:
    s = matches(pattern)
    total2 += s
    if s:
        total += 1

print(total)
print(total2)
