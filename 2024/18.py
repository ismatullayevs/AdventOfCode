import sys
import collections
import functools
import heapq

filename = 'test.txt' if len(sys.argv) < 2 else 'input.txt'


def solve(f=None):
    with open(filename) as file:
        coords = [tuple(map(int, line.strip().split(','))) for line in file]
    
    f = f or 1024
    R, C = 71, 71
    grid = [['.'] * C for _ in range(R)]

    for c, r in coords[:f]:
        grid[r][c] = '#'
    
    heap = [(0, 0, 0)]
    visited = {(0, 0)}
    while heap:
        cost, r, c = heapq.heappop(heap)
        if (r, c) == (R-1, C-1):
            return cost
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#' and (nr, nc) not in visited:
                visited.add((nr, nc))
                heapq.heappush(heap, (cost + 1, nr, nc))
    
    return -1


def solve2():
    with open(filename) as file:
        coords = [tuple(map(int, line.strip().split(','))) for line in file]
    
    l, r = 0, len(coords)-1
    while l < r:
        m = (l + r) // 2
        if solve(m) == -1:
            r = m
        else:
            l = m + 1
    return coords[l-1]


print(f"First part: {solve()}")
print(f"Second part: {solve2()}")
