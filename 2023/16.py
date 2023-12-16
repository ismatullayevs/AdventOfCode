import sys


filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()
    lines = content.split('\n')
    

def part_one(r, c, d):
    dirs = {'/': {(0, 1): [(-1, 0)], (1, 0): [(0, -1)], (0, -1): [(1, 0)], (-1, 0): [(0, 1)]},
            '\\': {(0, 1): [(1, 0)], (1, 0): [(0, 1)], (0, -1): [(-1, 0)], (-1, 0): [(0, -1)]},
            '|': {(0, 1): [(1, 0), (-1, 0)], (1, 0): [(1, 0)], (0, -1): [(1, 0), (-1, 0)], (-1, 0): [(-1, 0)]},
            '-': {(0, 1): [(0, 1)], (1, 0): [(0, 1), (0, -1)], (0, -1): [(0, -1)], (-1, 0): [(0, 1), (0, -1)]},}
    grid = [[c for c in line] for line in lines]
    R, C = len(grid), len(grid[0])
    energized = set()
    queue = [(r, c, d)]
    checked = set()

    while queue:
        r, c, d = queue.pop(0)
        energized.add((r, c))
        checked.add((r, c, d))

        if grid[r][c] == '.':
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < R and 0 <= nc < C:
                queue.append((nr, nc, d))
            continue
        
        for nd in dirs[grid[r][c]][d]:
            nr, nc = r + nd[0], c + nd[1]
            if 0 <= nr < R and 0 <= nc < C and not (nr, nc, nd) in checked:
                queue.append((nr, nc, nd))
        
    return len(energized)
            
        
def part_two():
    grid = [[c for c in line] for line in lines]
    R, C = len(grid), len(grid[0])
    left = [(r, 0, [(0, 1)]) for r in range(1, R-1)]
    bottom = [(R-1, c, [(-1, 0)]) for c in range(1, C-1)]
    right = [(r, C-1, [(0, -1)]) for r in range(1, R-1)]
    top = [(0, c, [(1, 0)]) for c in range(1, C-1)]
    starting_pos = left + right + top + bottom
    starting_pos.extend([(0, 0, [(1, 0), (0, 1)]), (0, C-1, [(1, 0), (0, -1)]), (R-1, 0, [(-1, 0), (0, 1)]), (R-1, C-1, [(-1, 0), (0, -1)])])

    res = 0
    for r, c, dirs in starting_pos:
        for d in dirs:
            res = max(res, part_one(r, c, d))
    
    return res


print(f"Part one: {part_one(0, 0, (0, 1))}")
print(f"Part two: {part_two()}")
