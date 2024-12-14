import sys
import collections
import functools

filename = 'test.txt' if len(sys.argv) < 2 else 'input.txt'


def solve():
    p, v = [], []
    with open(filename) as file:
        for line in file:
            a, b = line.split(' ')
            _, coor = a.split('=')
            p.append(list(map(int, coor.split(','))))
            _, vel = b.split('=')
            v.append(list(map(int, vel.split(','))))
    X, Y = 101, 103
    s = 100
    newp = []
    for i in range(len(p)):
        x, y = p[i]  # 0, 4
        vx, vy = v[i]  # 3, -3
        fx, fy = (x + s * vx) % X, (y + s * vy) % Y
        newp += [(fx, fy)]
    p = newp
    q1, q2, q3, q4 = 0, 0, 0, 0
    for x, y in p:
        if X % 2 == 1 and x == X // 2:
            continue
        if Y % 2 == 1 and y == Y // 2:
            continue

        if x < X // 2 and y < Y // 2:
            q1 += 1
        elif x >= X // 2 and y < Y // 2:
            q2 += 1
        elif x < X // 2 and y >= Y // 2:
            q3 += 1
        else:
            q4 += 1

    print(q1, q2, q3, q4)
    return q1 * q2 * q3 * q4


def solve2():
    p, v = [], []
    with open(filename) as file:
        for line in file:
            a, b = line.split(' ')
            _, coor = a.split('=')
            p.append(list(map(int, coor.split(','))))
            _, vel = b.split('=')
            v.append(list(map(int, vel.split(','))))
    X, Y = 101, 103
    newp = []
    s = 0
    while s < 10**9:
        for i in range(len(p)):
            x, y = p[i]
            vx, vy = v[i]
            fx, fy = (x + vx) % X, (y + vy) % Y
            newp += [(fx, fy)]
        p = newp
        newp = []
        s += 1
        if len(p) == len(set(p)):
            return s


print(f"First part: {solve()}")
print(f"Second part: {solve2()}")
