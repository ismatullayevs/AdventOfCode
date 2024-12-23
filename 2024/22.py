import sys
import collections
import functools

filename = 'test.txt' if len(sys.argv) < 2 else 'input.txt'


def solve():
    with open(filename) as file:
        data = [int(x) for x in file.read().splitlines()]

    res = 0
    for secret in data:
        k = secret
        for i in range(2000):
            k = k ^ (k * 64) % 16777216
            k = k ^ (k // 32) % 16777216
            k = k ^ (k * 2048) % 16777216
        res += secret
    
    return res


def solve2():
    with open(filename) as file:
        data = [int(x) for x in file.read().splitlines()]

    res = 0
    d = [dict() for _ in range(len(data))]
    for j, secret in enumerate(data):
        k = secret
        diff = []

        for i in range(2000):
            prev = k
            k = k ^ (k * 64) % 16777216
            k = k ^ (k // 32) % 16777216
            k = k ^ (k * 2048) % 16777216
            diff.append(k % 10 - prev % 10)
            if len(diff) >= 4 and not tuple(diff[-4:]) in d[j]:
                d[j][tuple(diff[-4:])] = k % 10
    
    checked = set()
    res = float('-inf')
    for i in range(len(d)):
        dd = d[i]
        for k in dd:
            if k in checked:
                continue
            checked.add(k)
            v = 0
            for j in range(len(d)):
                if k in d[j]:
                    v += d[j][k]
            
            res = max(res, v)
    return res


print(f"First part: {solve()}")
print(f"Second part: {solve2()}")
