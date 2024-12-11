import sys
from functools import cache

filename = 'test.txt' if len(sys.argv) < 2 else 'input.txt'


def solve():
    with open(filename, "r") as f:
        s = f.read().split()
    
    s = [int(x) for x in s]
    for i in range(25):
        ns = []
        for stone in s:
            ss = str(stone)
            if stone == 0:
                ns.append(1)
            elif len(ss) % 2 == 0:
                ns.append(int(ss[:len(ss)//2]))
                ns.append(int(ss[len(ss)//2:]))
            else:
                ns.append(2024 * stone)
        s = ns
    return len(s)

def solve2():
    with open(filename, "r") as f:
        s = f.read().split()

    @cache
    def dfs(stone, steps=0):
        s = 0
        ss = str(stone)
        if steps >= 75: return 1
        if stone == 0:
            return dfs(1, steps+1)
        if len(ss) % 2 == 0:
            s += dfs(int(ss[:len(ss)//2]), steps+1)
            s += dfs(int(ss[len(ss)//2:]), steps+1)
        else:
            s += dfs(stone * 2024, steps+1)
        return s

    s = [int(x) for x in s]
    res = 0
    for stone in s:
        res += dfs(stone)
    return res

print(f"First part: {solve()}")
print(f"Second part: {solve2()}")
