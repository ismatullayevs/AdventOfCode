import sys
from collections import defaultdict


filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()
    lines = content.split('\n')


def solution(part2):
    # I visualized the data using matplotlib to find remove and start nodes. See 25-visual.py
    graph = defaultdict(list)
    remove = [('sgc', 'xvk'), ('pzc', 'vps'), ('cvx', 'dph')]
    for line in lines:
        src, dsts = line.split(': ')
        dsts = dsts.split(' ')
        for dst in dsts:
            if (src, dst) in remove or (dst, src) in remove:
                continue
            graph[src].append(dst)
            graph[dst].append(src)
    
    res = 1
    start = ['lhl', 'vhm']
    for node in start:
        seen = set()
        queue = [node]

        while queue:
            node = queue.pop(0)
            if node in seen:
                continue
            seen.add(node)
            queue.extend(graph[node])
    
        res *= len(seen)
    
    return res


for part2 in [False]:
    print(f"Part {2 if part2 else 1}: {solution(part2)}")