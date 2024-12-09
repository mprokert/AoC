import itertools

data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

total = 0

for l in data.splitlines():
    result, numbers = l.split(":")
    result = int(result)
    numbers = [int(x) for x in numbers.split()]
    operators = itertools.product("am", repeat=len(numbers)-1)

    for o in operators:
        x = numbers[0]
        for op, y in zip(o, numbers[1:]):
            if op == "a":
                x += y
            else:
                x *= y
        if x == result:
            total += result
            break

print(total)

total = 0

for l in data.splitlines():
    result, numbers = l.split(":")
    result = int(result)
    numbers = [int(x) for x in numbers.split()]
    operators = itertools.product("amc", repeat=len(numbers)-1)

    for o in operators:
        x = numbers[0]
        for op, y in zip(o, numbers[1:]):
            if op == "a":
                x += y
            elif op == "m":
                x *= y
            else:
                x = int(str(x)+str(y))

        if x == result:
            total += result
            break

print(total)
