import sys
from collections import deque


filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()
    lines = content.split('\n')
    

def part_one():
    grid = []
    curr = 0, 0, 0
    for i, line in enumerate(lines):
        lst = []
        for j, char in enumerate(line):
            lst.append(char)
            if char == 'S':
                curr = i, j, 0
        grid.append(lst)

    q = deque((curr,))
    res, target_level = 0, 6
    checked = set()

    while q:
        i, j, steps = q.popleft()

        if (i,j) in checked:
            continue

        checked.add((i,j))

        if steps > target_level:
            break

        if steps % 2 == 0:
            res += 1

        for dir in ((0,1), (0,-1), (1,0), (-1,0)):
            new_i, new_j = i + dir[0], j + dir[1]
            if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]):
                if grid[new_i][new_j] != '#':
                    q.append((new_i, new_j, steps+1))
        
    return res


def part_two():
    grid = []
    curr = 0, 0, 0
    for i, line in enumerate(lines):
        lst = []
        for j, char in enumerate(line):
            lst.append(char)
            if char == 'S':
                curr = i, j, 0
        grid.append(lst)

    q = deque((curr,))
    res, target_level = 0, 26501365
    checked = set()
    R, C = len(grid), len(grid[0])

    while q:
        i, j, steps = q.popleft()
        print(steps)
        if (i,j) in checked:
            continue

        checked.add((i,j))

        if steps > target_level:
            continue

        if steps % 2 == 1:
            res += 1

        for dir in ((0,1), (0,-1), (1,0), (-1,0)):
            new_i, new_j = i + dir[0], j + dir[1]
            if grid[new_i%R][new_j%C] != '#':
                q.append((new_i, new_j, steps+1))
        
    return res


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")
