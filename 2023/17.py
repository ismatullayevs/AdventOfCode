import sys
from collections import defaultdict
import time
from heapq import heappush, heappop


filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()
    lines = content.split('\n')


def solution(part2):
    grid = [[int(d) for d in line] for line in lines]
    R, C = len(grid), len(grid[0])
    processed = set()
    pq = [(0, 0, 0, (), 0)]
    max_limit = 10 if part2 else 3
    min_limit = 4 if part2 else 0
    while pq:
        h, r, c, prev_dir, streak = heappop(pq)

        if (r, c, prev_dir, streak) in processed:
            continue

        processed.add((r, c, prev_dir, streak))
 
        for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if prev_dir and streak < min_limit and prev_dir != dir:
                continue
            dr, dc = dir
            nr, nc = r+dr, c+dc
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            if prev_dir and prev_dir == (-dr, -dc):
                continue
            if streak >= max_limit and prev_dir == dir:
                continue

            st = streak + 1 if prev_dir == dir else 1
            heappush(pq, (h + grid[nr][nc], nr, nc, dir, st))

        if r == R-1 and c == C-1:
            return h



for part2 in [False, True]:
    start = time.time()
    print(f"Part {'two' if part2 else 'one'}: {solution(part2)}")
    print(f"Runtime: {time.time() - start}s")