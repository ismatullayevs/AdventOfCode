import sys


filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()
    lines = content.split('\n')


def part_one():
    grid = [[c for c in line] for line in lines]
    R, C, load = len(grid), len(grid[0]), 0

    for c in range(C):
        sr, sc = 0, 0

        for r in range(R):
            if grid[r][c] == 'O':
                sc += 1

            if grid[r][c] == '#' or r == R - 1:
                a, b = R-sr-sc+1, R-sr
                load += (a+b)*(b-a+1)//2
                sr, sc = r+1, 0

    return load


def part_two():
    grid = [[c for c in line] for line in lines]
    R, C = len(grid), len(grid[0])

    def spin(grid):
        R, C = len(grid), len(grid[0])
        for c in range(C):
            for _ in range(R):
                for r in range(R):
                    if r > 0 and grid[r][c]=='O' and grid[r-1][c]=='.':
                        grid[r][c]='.'
                        grid[r-1][c] = 'O'
        return grid

    rem, cache = 10**9, {}
    while rem > 0:
        for _ in range(4):
            grid = spin(grid)
            grid = [list(row) for row in zip(*grid[::-1])]
        
        tgrid = tuple(tuple(row) for row in grid)
        if tgrid in cache:
            cycle = cache[tgrid] - rem
            rem %= cycle
        cache[tgrid] = rem
        rem -= 1
    
    load = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'O':
                load += R-r
    
    return load

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")
