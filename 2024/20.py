import sys
import collections
import functools
import heapq


filename = 'test.txt' if len(sys.argv) < 2 else 'input.txt'


def solve():
    with open(filename) as file:
        grid = [list(line.strip()) for line in file]
    R, C = len(grid), len(grid[0])
    sr, sc = 0, 0
    er, ec = 0, 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'S':
                sr, sc = r, c
                break
            if grid[r][c] == 'E':
                er, ec = r, c
                break
    
    tr = 100
    ans = 0
    opt = float('inf')
    heap = [(0, 0, sr, sc)]
    costs = {(sr, sc): 0}

    while heap:
        time, cost, r, c = heapq.heappop(heap)
        if time == 2:
            if (r, c) in costs and costs[(r, c)] - cost >= tr:
                ans += 1
            continue
        
        if grid[r][c] == 'E':
            if time == 0:
                opt = min(opt, cost)
            continue
            

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                ncost = cost + 1
                ntime = time

                if (nr, nc) in costs and costs[(nr, nc)] <= ncost:
                    continue

                if ntime == 1 or grid[nr][nc] == '#':
                    ntime += 1
                
                if ntime == 0:
                    costs[(nr, nc)] = ncost
                heapq.heappush(heap, (ntime, ncost, nr, nc))

    return ans

def solve2():
    with open(filename) as file:
        grid = [list(line.strip()) for line in file]
    R, C = len(grid), len(grid[0])
    sr, sc = 0, 0
    er, ec = 0, 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'S':
                sr, sc = r, c
                break
            if grid[r][c] == 'E':
                er, ec = r, c
                break
    
    tr = 100
    ans = 0
    opt = float('inf')
    heap = [(0, 0, sr, sc)]
    costs = {(sr, sc): 0}

    while heap:
        time, cost, r, c = heapq.heappop(heap)
        
        if grid[r][c] == 'E':
            if time == 0:
                opt = min(opt, cost)
            continue

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            ncost = cost + 1
            ntime = time
            if 0 <= nr < R and 0 <= nc < C:
                if (nr, nc) in costs or grid[nr][nc] == '#':
                    continue
                costs[(nr, nc)] = ncost
                heapq.heappush(heap, (ntime, ncost, nr, nc))

    for cr, cc in costs.keys():
        if (cr, cc) == (er, ec):
            continue
        for r in range(cr-20, cr+21):
            for c in range(cc-20, cc+21):
                if not (0 <= r < R and 0 <= c < C) or (r, c) == (cr, cc) or grid[r][c] == '#' or (r, c) not in costs:
                    continue
                dist = abs(r-cr) + abs(c-cc)
                if dist <= 20 and costs[(r, c)] - (costs[(cr, cc)] + dist) >= tr:
                    ans += 1

    return ans


print(f"First part: {solve()}")
print(f"Second part: {solve2()}")
