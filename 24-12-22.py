data = """1
2
3
2024"""

from collections import Counter

def next_secret(num, depth=1):
    ones = [num%10]
    while depth:
        num = ((64*num)^ num) % 16777216
        num = (num//32 ^ num) % 16777216
        num = (2048 * num ^ num) % 16777216
        depth -= 1
        ones.append(num%10)
        if not depth:
            return num, ones

total = 0

change_map = Counter()

for x in data.splitlines():
    num, ones = next_secret(int(x), 2000)
    total += num

    diff = [ones[x] - ones[x-1] for x in range(1, len(ones))]

    local_count = Counter()

    for i in range(4, len(diff)):
        k = tuple(diff[i-4:i])
        if k not in local_count:
            local_count[k] = ones[i]

    change_map.update(local_count)

print(total)

print(change_map.most_common(1))

changes = {}