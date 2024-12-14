import sys

data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


class Machine:
    def __init__(self, a, b, p, p2=False):
        self.a = complex(int(a[0]), int(a[1]))
        self.b = complex(int(b[0]), int(b[1]))
        self.p = complex(int(p[0]), int(p[1]))
        if p2:
            self.p = complex(10000000000000+int(p[0]), 10000000000000+int(p[1]))

    def solve(self):
        tokens = sys.maxsize
        for i in range(100):
            for j in range(100):
                if (3 * i + j) < tokens:
                    if self.p == i * self.a + j * self.b:
                        tokens = 3*i + j
        return tokens if tokens < sys.maxsize else 0

    def solve2(self):
        det = self.a.real * self.b.imag - self.b.real * self.a.imag
        if det == 0:
            return 0
        deti = self.p.real * self.b.imag - self.p.imag * self.b.real
        detj = self.a.real * self.p.imag - self.a.imag * self.p.real

        i = deti/det
        j = detj/det
        if int(i) == i and int(j) == j:
            return 3*i + j
        return 0

    def solve3(self):
        t1, t2 = 3, 1
        token = 0
        if self.b.real > self.b.imag:
            self.a, self.b = self.b, self.a
            t1, t2 = 1, 3
        if self.a.real <= self.a.imag or self.b.real >= self.b.imag:
            raise ValueError

        while True:
            if self.p.real > self.p.imag > 0:
                i = max(int(self.p.real / self.a.real / 2) - 1, 1)
                self.p -= i * self.a
                token += t1 * i
            elif self.p.imag >= self.p.real > 0:
                i = max(int(self.p.imag / self.b.imag / 2) - 1, 1)
                self.p -= i * self.b
                token += t2 * i
            if self.p.imag < 0 or self.p.real < 0:
                token = 0
                break
            if self.p.imag == 0 and self.p.real == 0:
                break
        return token

import re

rexa = re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
rexb = re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
rexp = re.compile(r"Prize: X=(\d+), Y=(\d+)")

token = 0
token2 = 0

a = rexa.findall(data)
b = rexb.findall(data)
p = rexp.findall(data)

for ba, bb, p in zip(a, b, p):
    token += Machine(ba, bb, p).solve2()
    token2 += Machine(ba, bb, p, True).solve2()

print(int(token))
print(int(token2))
