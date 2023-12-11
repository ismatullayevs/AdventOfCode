import sys


filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()
    lines = content.split('\n')


def part_one():
    available = {'|': ((1, 0), (-1, 0)), '-': ((0, 1), (0, -1)), 'J': ((-1, 0), (0, -1)), 'L': ((-1, 0), (0, 1)), 
                 '7': ((0, -1), (1, 0)), 'F': ((0, 1), (1, 0)), 'S': ((1, 0), (-1, 0))}
    start = (0, 0)
    grid = []
    for i, line in enumerate(lines):
        grid.append(list(line))
        for j, c in enumerate(line):
            if c == 'S':
                start = i, j    
    r, c = start
    steps = 0
    previous_pos = None
    while not (steps != 0 and grid[r][c] == 'S'):
        for dir in available[grid[r][c]]:
            if (r + dir[0], c + dir[1]) == previous_pos:
                continue
            previous_pos = r, c
            r, c = r + dir[0], c + dir[1]
            steps += 1
            break
    return steps // 2


def part_two():
    # No need to find S. Just replace S with | in input file
    grid = [list(line) for line in lines]
    grid_3x = [[' '] * (len(grid[0]) * 3) for _ in range(len(grid) * 3)]

    fill = {'F': [(0, 1, '-'), (1, 0, '|')], '-': [(0, 1, '-'), (0, -1, '-')], 
            '|': [(1, 0, '|'), (-1, 0, '|')], 'J': [(-1, 0, '|'), (0, -1, '-')],
            'L': [(-1, 0, '|'), (0, 1, '-')], '7': [(0, -1, '-'), (1, 0, '|')]}
    dirs = {(0, 1), (0, -1), (1, 0), (-1, 0)}

    dots = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            gi, gj = i * 3 + 1, j * 3 + 1
            grid_3x[gi][gj] = grid[i][j]
            if grid[i][j] in fill:
                for dir in fill[grid[i][j]]:
                    grid_3x[gi + dir[0]][gj + dir[1]] = dir[2]
            if grid[i][j] == '.':
                dots += 1

    # needs debugging 
    queue, checked = [(0, 0)], set()
    dotcount = 0
    while queue:
        r, c = queue.pop(0)
        if (r, c) in checked: continue
        checked.add((r, c))
        if grid_3x[r][c] == '.':
            dotcount += 1
        for dir in dirs:
            nr, nc = r + dir[0], c + dir[1]
            if len(grid_3x) > nr >= 0 and len(grid_3x[0]) > nc >= 0 and grid_3x[nr][nc] not in fill and (nr, nc) not in checked:
                queue.append((nr, nc))

    return dots - dotcount


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")
