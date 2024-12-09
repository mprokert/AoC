data = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

import re

muls_ex = re.compile(r"mul\((\d+),(\d+)\)")

total = 0
total2 = 0

for x, y in muls_ex.findall(data):
    total += int(x) * int(y)

print(total)

dos = [0]
donts = []
i = 0

while True:
    do = data.find("do()", i)
    dont = data.find("don't()", i)
    if do == -1 and dont == -1:
        break
    if do == -1:
        donts.append(dont)
        break
    if dont == -1:
        dos.append(do)
        break
    if do < dont:
        dos.append(do)
        i = do+1
    else:
        donts.append(dont)
        i = dont+1

dos.reverse()
donts.reverse()
do = 0
dont = donts.pop()
end = False

while True:
    for x, y in muls_ex.findall(data[do:dont]):
        total2 += int(x) * int(y)

    while do < dont:
        try:
            do = dos.pop()
        except IndexError:
            end = True
            break

    while dont < do:
        try:
            dont = donts.pop()
        except IndexError:
            end = True
            break

    if end:
        break

if do > dont:
    for x, y in muls_ex.findall(data[do:]):
        total2 += int(x) * int(y)

print(total2)
