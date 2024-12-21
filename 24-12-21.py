import itertools
import sys

data="""029A
980A
179A
456A
379A"""

keypad = {
    "7": 0+0j,
    "8": 1+0j,
    "9": 2+0j,
    "4": 0+1j,
    "5": 1+1j,
    "6": 2+1j,
    "1": 0+2j,
    "2": 1+2j,
    "3": 2+2j,
    "0": 1+3j,
    "A": 2+3j,
}

directions = {
    "u": -1j,
    "d": 1j,
    "l": -1,
    "r": 1
}

from collections import Counter

def get_dir_path(start, end):
    if start == end:
        return "A"
    if start == "u":
        if end == "A":
            return "rA"
        if end == "l":
            return "dlA"
        if end == "r":
            return "drA"
    if start == "A":
        if end == "u":
            return "lA"
        if end == "r":
            return "dA"
        if end == "d":
            return "ldA"
        if end == "l":
            return "dllA"
    if start == "l":
        if end == "u":
            return "ruA"
        if end == "d":
            return "rA"
        if end == "A":
            return "rruA"
    if start == "d":
        if end == "l":
            return "lA"
        if end == "r":
            return "rA"
        if end == "A":
            return "urA"
    if start == "r":
        if end == "u":
            return "luA"
        if end == "d":
            return "lA"
        if end == "A":
            return "uA"

def get_key_combis(start, end):
    d = keypad[end]-keypad[start]
    dx, dy = int(d.real), int(d.imag)
    dirs = ""
    if dx > 0:
        dirs += dx * "r"
    else:
        dirs += -dx * "l"
    if dy > 0:
        dirs += dy * "d"
    else:
        dirs += -dy * "u"
    combis = set(itertools.permutations(dirs))
    for combi in list(combis):
        x = keypad[start]
        for ch in combi:
            x += directions[ch]
            if x not in keypad.values():
                combis.remove(combi)
                break
    return ["".join(combi) + "A" for combi in list(combis)]


def get_key_sequence(seq):
    sequence = []
    start = "A"
    for ch in seq:
        sequence.append(get_key_combis(start, ch))
        start = ch
    for elem in itertools.product(*sequence):
        yield "".join(elem)

def get_dir_sequence(counter):
    new_c = Counter()
    for s, fac in counter.items():
        start = "A"
        for ch in s:
            sequence = get_dir_path(start, ch)
            start = ch
            new_c[sequence] += fac
    return new_c

total = 0
for lin in data.splitlines():
    shortest = sys.maxsize
    for sequence in get_key_sequence(lin):
        counter = Counter()
        for s in sequence.split("A"):
            counter[s+"A"] += 1
        counter["A"] -= 1
        for i in range(2):
            counter = get_dir_sequence(counter)
        total_len = 0
        for k in counter:
            total_len += len(k) * counter[k]
        if total_len < shortest:
            sc = counter
            shortest = total_len
    total += shortest * int(lin.replace("A", ""))

print(total)

total = 0
for lin in data.splitlines():
    shortest = sys.maxsize
    seq = ""
    for sequence in get_key_sequence(lin):
        counter = Counter()
        for s in sequence.split("A"):
            counter[s+"A"] += 1
        counter["A"] -= 1
        for i in range(25):
            counter = get_dir_sequence(counter)
        total_len = 0
        for k in counter:
            total_len += len(k) * counter[k]
        if total_len < shortest:
            shortest = total_len
    total += shortest * int(lin.replace("A", ""))

print(total)
