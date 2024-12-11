import sys
from functools import cache

filename = 'test.txt' if len(sys.argv) < 2 else 'input.txt'


def solve():
    with open(filename) as f:
        mx = f.read().splitlines()
        mx = [list(l) for l in mx]

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    R, C = len(mx), len(mx[0])
    res = 0

    @cache
    def dfs(x, y) -> set:
        nines = set()
        if mx[x][y] == '9':
            nines.add((x, y))
            return nines

        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < R and 0 <= ny < C and int(mx[nx][ny]) == int(mx[x][y]) + 1:
                nines |= dfs(nx, ny)

        return nines

    for i in range(R):
        for j in range(C):
            if mx[i][j] == '0':
                v = dfs(i, j)
                res += len(v)

    return res


def solve2():
    with open(filename) as f:
        mx = f.read().splitlines()
        mx = [list(l) for l in mx]

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    R, C = len(mx), len(mx[0])
    res = 0

    @cache
    def dfs(x, y) -> int:
        score = 0
        if mx[x][y] == '9':
            score = 1
            return score

        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < R and 0 <= ny < C and int(mx[nx][ny]) == int(mx[x][y]) + 1:
                score += dfs(nx, ny)

        return score

    for i in range(R):
        for j in range(C):
            if mx[i][j] == '0':
                res += dfs(i, j)

    return res


print(f"First part: {solve()}")
print(f"Second part: {solve2()}")
