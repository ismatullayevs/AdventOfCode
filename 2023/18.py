import sys


filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()
    lines = content.split('\n')
    

def part_one():
    dirs = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    vertices, edges, curr = [], 0, (0, 0)
    
    for line in lines:
        d, s, _ = line.split(' ')
        edges += int(s)
        curr = (curr[0] + dirs[d][0] * int(s), curr[1] + dirs[d][1] * int(s))
        vertices.append(curr)
    
    area = 0
    for i in range(len(vertices)):
        area += vertices[i][0] * vertices[(i + 1) % len(vertices)][1]
        area -= vertices[i][1] * vertices[(i + 1) % len(vertices)][0]
    area = abs(area) / 2
    area = area + edges / 2 + 1
    # shoelace + pick's theorem as explained here: youtube.com/watch?v=bGWK76_e-LM

    return int(area)


def part_two():
    ntd = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
    dirs = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    vertices, edges, curr = [], 0, (0, 0)
    
    for line in lines:
        _, _, c = line.split(' ')
        s, d = int(c[2:-2], 16), ntd[c[-2]]
        edges += s
        curr = (curr[0] + dirs[d][0] * int(s), curr[1] + dirs[d][1] * int(s))
        vertices.append(curr)
    
    area = 0
    for i in range(len(vertices)):
        area += vertices[i][0] * vertices[(i + 1) % len(vertices)][1]
        area -= vertices[i][1] * vertices[(i + 1) % len(vertices)][0]
    area = abs(area) / 2
    area = area + edges / 2 + 1

    return int(area)


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")
