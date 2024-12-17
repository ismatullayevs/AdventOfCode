import sys
import collections
import functools
import heapq
from z3 import *

filename = 'test.txt' if len(sys.argv) < 2 else 'input.txt'


def solve(a=0):
    a, b, c = a, 0, 0
    with open(filename) as file:
        lines = file.readlines()
    
    a = a or int(lines[0].split(': ')[1])
    b = int(lines[1].split(': ')[1])
    c = int(lines[2].split(': ')[1])

    res = []
    while a != 0:
        b = a % 8
        b = b ^ 1
        c = a // (1 << b)
        a = a // 8
        b = b ^ c
        b = b ^ 6
        res.append(b % 8)
    
    return ",".join(str(x) for x in res)

def solve2():
    a, b, c = 0, 0, 0
    with open(filename) as file:
        lines = file.readlines()
    
    nums = [int(x) for x in lines[4].split(': ')[1].strip().split(',')]

    opt = Optimize()
    s = BitVec('s', 64)
    a = s
    for x in nums:
        b = a % 8
        b = b ^ 1
        c = a / (1 << b)
        a = a / 8
        b = b ^ c
        b = b ^ 6
        opt.add((b % 8) == x)
    opt.add(a == 0)
    opt.minimize(s)
    assert str(opt.check()) == 'sat'
    return opt.model().eval(s)

print(f"First part: {solve()}")
print(f"Second part: {solve2()}")
