import sys
import collections
import functools
import math


filename = 'test.txt' if len(sys.argv) < 2 else 'input.txt'


def solve():
    m = []
    with open(filename, 'r') as f:
        m = f.read().split('\n\n')
        m = [x.splitlines() for x in m]
    res = 0

    for machine in m:
        x1, y1 = machine[0].split(': ')[1].split(', ')
        x2, y2 = machine[1].split(': ')[1].split(', ')

        x1, y1 = int(x1.split('+')[1]), int(y1.split('+')[1])
        x2, y2 = int(x2.split('+')[1]), int(y2.split('+')[1])

        x3, y3 = machine[2].split(': ')[1].split(', ')
        x3, y3 = int(x3.split('=')[1]), int(y3.split('=')[1])

        mt = float('inf')
        for i in range(0, 101):
            s = (x3 - i * x1) / x2
            if not s.is_integer(): continue
            if s > 101: continue
            if (y3 - i * y1) / y2 != s: continue

            if i * 3 + s < mt:
                mt = i * 3 + s

        res += mt if mt != float('inf') else 0
    return res


def solve2():
    m = []
    with open(filename, 'r') as f:
        m = f.read().split('\n\n')
        m = [x.splitlines() for x in m]
    res = 0

    for machine in m:
        x1, y1 = machine[0].split(': ')[1].split(', ')
        x2, y2 = machine[1].split(': ')[1].split(', ')

        x1, y1 = int(x1.split('+')[1]), int(y1.split('+')[1])
        x2, y2 = int(x2.split('+')[1]), int(y2.split('+')[1])

        x3, y3 = machine[2].split(': ')[1].split(', ')
        x3, y3 = int(x3.split('=')[1]), int(y3.split('=')[1])
        x3 += 10000000000000
        y3 += 10000000000000

        D = x1 * y2 - x2 * y1
        Dx = x3 * y2 - x2 * y3
        Dy = x1 * y3 - x3 * y1

        if D == 0:
            continue

        i = Dx / D
        s = Dy / D

        if not i.is_integer() or not s.is_integer():
            continue

        res += i * 3 + s
        
    return res


print(f"First part: {solve()}")
print(f"Second part: {solve2()}")
