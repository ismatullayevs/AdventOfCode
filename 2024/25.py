import sys
import collections
import functools

filename = 'test.txt' if len(sys.argv) < 2 else 'input.txt'


def solve():
    locks, keys = [], []
    with open(filename) as file:
        grids = file.read().split('\n\n')
    for grid in grids:
        grid = grid.split('\n')
        heights = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '#':
                    heights[j] += 1
        if grid[0][0] == '#':
            locks.append(heights)
        else:
            keys.append(heights)
    
    res = 0
    for lock in locks:
        for key in keys:
            if len(lock) != len(key):
                continue
            
            if all(a + b <= 7 for a, b in zip(lock, key)):
                res += 1
    
    return res


def solve2():
    pass


print(f"First part: {solve()}")
print(f"Second part: {solve2()}")
