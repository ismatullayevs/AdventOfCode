import sys
import collections
import functools

filename = 'test.txt' if len(sys.argv) < 2 else 'input.txt'


def solve():
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        mx = [list(line) for line in lines]

    R, C = len(mx), len(mx[0])
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    visited = set()
    res = 0
    for i in range(R):
        for j in range(C):
            if (i, j) in visited:
                continue
            visited.add((i, j))
            q = collections.deque([(i, j)])
            p, a = 0, 0
            while q:
                r, c = q.popleft()
                a += 1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and mx[nr][nc] == mx[r][c]:
                        if (nr, nc) in visited:
                            continue
                        visited.add((nr, nc))
                        q.append((nr, nc))
                    else:
                        p += 1
            res += a * p
    return res


def solve2():
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        mx = [list(line) for line in lines]

    R, C = len(mx), len(mx[0])
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    visited = set()
    res = 0

    def find(UF, x):
        if x != UF[x]:
            UF[x] = find(UF, UF[x])
        return UF[x]

    def union(UF, x, y):
        UF[find(UF, x)] = find(UF, y)

    for i in range(R):
        for j in range(C):
            if (i, j) in visited:
                continue
            visited.add((i, j))
            q = collections.deque([(i, j)])
            a, sides = 0, 0
            UF = {}
            while q:
                r, c = q.popleft()
                a += 1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and mx[nr][nc] == mx[r][c]:
                        if (nr, nc) in visited:
                            continue
                        visited.add((nr, nc))
                        q.append((nr, nc))
                    else:
                        br, bc = r+dr/2, c+dc/2
                        UF[(br, bc)] = (br, bc)
                        if dr == 0 and (br-1, bc) in UF and mx[r][c] == mx[r-1][c]:
                            union(UF, (br, bc), (br-1, bc))
                        if dr == 0 and (br+1, bc) in UF and mx[r][c] == mx[r+1][c]:
                            union(UF, (br, bc), (br+1, bc))
                        if dc == 0 and (br, bc+1) in UF and mx[r][c] == mx[r][c+1]:
                            union(UF, (br, bc), (br, bc+1))
                        if dc == 0 and (br, bc-1) in UF and mx[r][c] == mx[r][c-1]:
                            union(UF, (br, bc), (br, bc-1))

            sides = len(set(find(UF, x) for x in UF))
            res += a * sides
    return res


print(f"First part: {solve()}")
print(f"Second part: {solve2()}")
