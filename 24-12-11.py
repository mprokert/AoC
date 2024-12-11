data = """125 17"""

stones = [int(x) for x in data.split()]

cache = {}

def blink(stones):
    new_stones = []
    for stone in stones:
        digits = len(str(stone))
        if not stone:
            new_stones.append(1)
        elif not (digits % 2):
            half = digits//2
            new_stones.append(int(str(stone)[:half]))
            new_stones.append(int(str(stone)[half:]))
        else:
            new_stones.append(2024*stone)
    return new_stones

def blink25(stones):
    first = stones[0] if len(stones) == 1 else -1
    if len(stones) == 1:
        if first in cache:
            return cache[first]
    for _ in range(25):
        stones = blink(stones)
    if first > 0:
        cache[first] = stones
    return stones

stones = blink25(stones)
print(len(stones))

total = 0

stonemap = {}

for stone in stones:
    stonemap[stone] = stonemap.get(stone, 0) + 1

for stone in stonemap:
    stones2 = blink25([stone])

    stonemap2 = {}

    for stone2 in stones2:
        stonemap2[stone2] = stonemap2.get(stone2, 0) + 1

    for stone2 in stonemap2:
        total += len(blink25([stone2])) * stonemap2[stone2] * stonemap[stone]

print(total)
