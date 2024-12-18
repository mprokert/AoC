import sys

data = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""


class TBC:
    def __init__(self, a, b, c, program):
        self.a = a
        self.b = b
        self.c = c
        self.ip = 0
        self.program = program

        self.o = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv
        }
        self.out = ""

    def combo(self, val):
        if val <= 3:
            return val
        if val == 4:
            return self.a
        if val == 5:
            return self.b
        if val == 6:
            return self.c
        raise ValueError


    def adv(self, val):
        self.a  = self.a // 2**self.combo(val)

    def bxl(self, val):
        self.b = val ^ self.b

    def bst(self, val):
        self.b = self.combo(val) % 8

    def jnz(self, val):
        if self.a:
            self.ip = val-2

    def bxc(self, val):
        self.b = self.b ^ self.c

    def out(self, val):
        self.out += str(self.combo(val) % 8)

    def bdv(self, val):
        self.b  = self.a // 2**self.combo(val)

    def cdv(self, val):
        self.c  = self.a // 2**self.combo(val)

    def run(self, noprint=False):
        while self.ip+1 < len(self.program):
            self.o[self.program[self.ip]](self.program[self.ip + 1])
            self.ip += 2
        if not noprint:
            print(",".join([ch for ch in self.out]))

import re

a = int(re.search(r"Register A: (\d+)", data).group(1))
b = int(re.search(r"Register B: (\d+)", data).group(1))
c = int(re.search(r"Register C: (\d+)", data).group(1))
prog = data.split("Program: ")[-1]
program = [int(val) for val in prog.split(",")]
tbc = TBC(a, b, c, program)
tbc.run()

prog = prog.strip().replace(",", "")

def find_next(a):
    global lowest
    d = {}
    for i in range(8):
        tbc = TBC(a+i, b, c, program)
        tbc.run(noprint=True)
        d[a+i] = tbc.out
    for k, v in d.items():
        if k == 0 and v == "0":
            continue
        if prog == v:
            if k < lowest:
                lowest = k
            break
        elif prog.endswith(v):
            find_next(8*k)

lowest = sys.maxsize
find_next(0)
print(lowest)