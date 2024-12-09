data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

before_dict = {}
after_dict = {}
rules = []


for line in data.splitlines():
    if "|" in line.strip():
        before, after = [int(x) for x in (line.split("|"))]
        before_dict.setdefault(before, []).append(after)
        after_dict.setdefault(after, []).append(before)
    elif line.strip():
        rules.append([int(x) for x in line.split(",")])

correct_rules = []
incorrect_rules = []

def check(rule):
    error_index = 0
    for i in range(len(rule)):
        before = rule[:i]
        elem = rule[i]
        after = rule[i+1:]
        for b in before:
            if b in before_dict.get(elem, []):
                error_index = -i
                break

        for a in after:
            if a in after_dict.get(elem, []):
                error_index = i
                break

        if error_index:
            break
    return error_index

for rule in rules:
    error = check(rule)

    if not error:
        correct_rules.append(rule)
    else:
        incorrect_rules.append(rule)

total = 0
for rule in correct_rules:
    total += rule[len(rule)//2]

print(total)

fixed_rules = []

for rule in incorrect_rules:
    for i in range(1000):
        index = check(rule)
        if not index:
            fixed_rules.append(rule)
            break
        if index < 0:
            index = abs(index)
            rule = rule[:index-1] + [rule[index]] + [rule[index-1]] + rule[index+1:]
        else:
            rule = rule[:index] + rule[index+1:] + [rule[index]]

total2 = 0

for rule in fixed_rules:
    total2 += rule[len(rule)//2]

print(total2)
