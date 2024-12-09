data = """2333133121414131402"""

expanded = []
total_blocks = 0
for i, ch in enumerate(data):
    if not (i % 2):
        expanded += int(ch) * [i//2]
        total_blocks += int(ch)
    else:
        expanded += int(ch) * ["."]

compact = []

for elem in expanded[:]:
    if elem != ".":
        compact.append(elem)
    else:
        while True:
            next_item = expanded.pop()
            if next_item != ".":
                compact.append(next_item)
                break

    if len(compact) >= total_blocks:
        break

checksum = 0
for i, block in enumerate(compact):
    checksum += i * block

print(checksum)

# p2

expanded = []
max_id = 0

for i, ch in enumerate(data):
    if not (i % 2):
        expanded.append((int(ch), i//2))
        max_id = i//2
    else:
        if int(ch) > 0:
            expanded.append((int(ch), "."))

compact = []
final = []

for id_ in range(max_id, 1, -1):

    for i, elem in enumerate(expanded):
        if elem[1] == id_:
            expanded = expanded[:i] + [(elem[0], ".")] + expanded[i+1:]
            break

    for i, gap in enumerate(expanded):
        if gap[1] == "." and gap[0] >= elem[0]:
            if gap[0] == elem[0]:
                expanded = expanded[:i] + [(elem[0], elem[1])] + expanded[i+1:]
            else:
                expanded = expanded[:i] + [(elem[0], elem[1]), (gap[0] - elem[0], ".")] + expanded[i+1:]
            break

final = []
for l, ch in expanded:
    final += l*[ch]

checksum = 0
for i, block in enumerate(final):
    if block != ".":
        checksum += i * block

print(checksum)
