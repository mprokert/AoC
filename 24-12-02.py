data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def is_safe(l):
    check = [l[i]-l[i-1] for i in range(1, len(l))]
    return is_safe_cl(check)

def is_safe_cl(check):
    if min(check) > 0 and max(check) < 4:
        return True
    if min(check) > -4 and max(check) < 0:
        return True
    return False

def is_safe_dampened(l):
    if is_safe(l):
        return True

    for i in range(len(l)):
        new_l = l[:i] + l[i + 1:]
        if is_safe(new_l):
            return True
    return False

safe = 0
safe_damp = 0
for line in data.splitlines():
    ints = [int(x) for x in line.split()]
    if is_safe(ints):
        safe += 1
    if is_safe_dampened(ints):
        safe_damp += 1

print(safe)
print(safe_damp)
