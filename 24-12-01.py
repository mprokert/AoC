data = """3   4
4   3
2   5
1   3
3   9
3   3"""

list1 = []
list2 = []

for lin in data.splitlines():
    x, y = lin.split()
    list1.append(int(x))
    list2.append(int(y))

list1.sort()
list2.sort()

total = 0

for x, y in zip(list1, list2):
    total += abs(x - y)

print(total)

total2 = 0

for x in list1:
    total2 += x * list2.count(x)

print(total2)
