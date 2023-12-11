import sys
import numpy as np


filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()
    lines = content.split('\n')


def part_one():
    graph = np.array([list(line) for line in lines])
    emptry_rows = [i for i in range(len(graph)) if '#' not in graph[i]]
    empty_cols = [j for j in range(len(graph[0])) if '#' not in graph[:, j]]

    cs = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == '#':
                cs.append((i, j))

    ans = 0
    for i in range(len(cs)-1):
        for j in range(i + 1, len(cs)):
            steps = abs(cs[i][0] - cs[j][0]) + abs(cs[i][1] - cs[j][1])

            for row in emptry_rows:
                if cs[i][0] < row < cs[j][0] or cs[j][0] < row < cs[i][0]:
                    steps += 1
            
            for col in empty_cols:
                if cs[i][1] < col < cs[j][1] or cs[j][1] < col < cs[i][1]:
                    steps += 1

            ans += steps
    return ans


def part_two():
    graph = np.array([list(line) for line in lines])
    emptry_rows = [i for i in range(len(graph)) if '#' not in graph[i]]
    empty_cols = [j for j in range(len(graph[0])) if '#' not in graph[:, j]]

    cs = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == '#':
                cs.append((i, j))

    ans = 0
    for i in range(len(cs)-1):
        for j in range(i + 1, len(cs)):
            steps = abs(cs[i][0] - cs[j][0]) + abs(cs[i][1] - cs[j][1])

            for row in emptry_rows:
                if cs[i][0] < row < cs[j][0] or cs[j][0] < row < cs[i][0]:
                    steps += 999999
            
            for col in empty_cols:
                if cs[i][1] < col < cs[j][1] or cs[j][1] < col < cs[i][1]:
                    steps += 999999

            ans += steps
    return ans


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")
