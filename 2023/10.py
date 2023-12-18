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
    steps, vertices = 0, []
    previous_pos = None
    while not (steps != 0 and grid[r][c] == 'S'):
        for dir in available[grid[r][c]]:
            if (r + dir[0], c + dir[1]) == previous_pos:
                continue
            previous_pos = r, c
            if grid[r][c] not in '-|':
                vertices.append((r, c))
            r, c = r + dir[0], c + dir[1]
            steps += 1
            break
    
    area = 0
    for i in range(len(vertices)):
        area += vertices[i][0] * vertices[(i + 1) % len(vertices)][1]
        area -= vertices[i][1] * vertices[(i + 1) % len(vertices)][0]
    area = abs(area) // 2
    print(area)
    return int(area - steps/2 + 1)


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")
