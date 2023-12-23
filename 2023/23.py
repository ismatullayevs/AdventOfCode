import sys
from collections import deque


filename = '/home/coder/aoc/2023/example.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()
    lines = content.split('\n')


def solution(part2):
    grid = [list(ch) for ch in lines]
    can_move = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}
    R, C = len(grid), len(grid[0])

    def dfs(curr_dir, prev_dir=None, history=None):
        if history is None: history = set()
        steps, ways = 0, []
        r, c = curr_dir
        q = deque(((r, c, prev_dir),))
        while q:
            r, c, prev_dir = q.popleft()
            if (r, c) in history: return 0
            history.add((r, c))
            steps += 1

            if r == R-1 and c == C-2:
                return steps

            for dr, dc in can_move.values():
                if (-dr, -dc) == prev_dir: continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
                    if grid[nr][nc] == '.':
                        q.append((nr, nc, (dr, dc)))
                        break
                    if (dr, dc) == can_move[grid[nr][nc]] or part2:
                        ways.append(dfs((nr, nc), (dr, dc), history.copy()))

        if not ways or not any(ways):
            return 0        
        
        return steps + max(ways)


    return dfs((0, 1)) - 1


for part2 in [False, True]:
    print(solution(part2))