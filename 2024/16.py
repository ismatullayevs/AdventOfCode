import sys
import collections
import heapq

filename = 'test.txt' if len(sys.argv) < 2 else 'input.txt'


def solve():
    with open(filename, 'r') as f:
        mx = f.read().splitlines()
    mx = [list(x) for x in mx]
    R, C = len(mx), len(mx[0])
    sr, sc = 0, 0
    er, ec = 0, 0
    for r in range(R):
        for c in range(C):
            if mx[r][c] == 'S':
                sr, sc = r, c
            if mx[r][c] == 'E':
                er, ec = r, c

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = {(sr, sc)}
    heap = [(0, sr, sc, (0, 1))]
    while heap:
        cost, r, c, dir = heapq.heappop(heap)
        if mx[r][c] == 'E':
            return cost

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and mx[nr][nc] != '#' and (nr, nc) not in visited:
                visited.add((nr, nc))
                newcost = 1
                if dir != (dr, dc):
                    newcost += 1000
                heapq.heappush(heap, (cost + newcost, nr, nc, (dr, dc)))
    return -1


def solve2():
    with open(filename, 'r') as f:
        mx = f.read().splitlines()
    mx = [list(x) for x in mx]
    R, C = len(mx), len(mx[0])
    sr, sc = 0, 0
    er, ec = 0, 0
    for r in range(R):
        for c in range(C):
            if mx[r][c] == 'S':
                sr, sc = r, c
            if mx[r][c] == 'E':
                er, ec = r, c

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    heap = [(0, sr, sc, (0, 1))]
    visited = {(sr, sc, (0, 1)): 0}
    parents = collections.defaultdict(list)
    min_cost = None
    while heap:
        cost, r, c, (ddr, ddc) = heapq.heappop(heap)
        if r == er and c == ec:
            min_cost = cost
            break
        
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and mx[nr][nc] != '#':
                if (dr, dc) == (-ddr, -ddc):
                    continue

                if (dr, dc) == (ddr, ddc):
                    if (nr, nc, (dr, dc)) in visited and visited[(nr, nc, (dr, dc))] <= cost + 1:
                        if visited[(nr, nc, (dr, dc))] == cost + 1:
                            parents[(nr, nc, (dr, dc))].append((r, c, (ddr, ddc)))
                        continue
                    visited[(nr, nc, (dr, dc))] = cost + 1
                    parents[(nr, nc, (dr, dc))].append((r, c, (ddr, ddc)))
                    heapq.heappush(heap, (cost + 1, nr, nc, (dr, dc)))
                else:
                    if (r, c, (dr, dc)) in visited and visited[(r, c, (dr, dc))] <= cost + 1000:
                        if visited[(r, c, (dr, dc))] == cost + 1000:
                            parents[(r, c, (dr, dc))].append((r, c, (ddr, ddc)))
                        continue
                    visited[(r, c, (dr, dc))] = cost + 1000
                    parents[(r, c, (dr, dc))].append((r, c, (ddr, ddc)))
                    heapq.heappush(heap, (cost + 1000, r, c, (dr, dc)))

    ans = set()
    path = {(er, ec, (0, 1))}
    def dfs(r, c, dr, dc, points):
        nonlocal ans
        if points < 0:
            return
        
        if r == sr and c == sc:
            ans |= path
            return

        for pr, pc, (pdr, pdc) in parents[(r, c, (dr, dc))]:
            path.add((pr, pc, (pdr, pdc)))
            if (pr, pc) == (r, c):
                dfs(pr, pc, pdr, pdc, points - 1000)
            else:
                dfs(pr, pc, pdr, pdc, points - 1)
            path.remove((pr, pc, (pdr, pdc)))

    dfs(er, ec, 0, 1, min_cost-1000)
    answer = set()
    for r, c, (dr, dc) in ans:
        answer.add((r, c))
    return len(answer)
print(f"First part: {solve()}")
print(f"Second part: {solve2()}")
