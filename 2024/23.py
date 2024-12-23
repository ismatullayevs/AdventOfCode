import sys
import collections
import functools

filename = 'test.txt' if len(sys.argv) < 2 else 'input.txt'


def solve():
    graph = collections.defaultdict(list)
    with open(filename) as file:
        data = file.read().splitlines()
        for line in data:
            a, b = line.split('-')
            graph[a].append(b)
            graph[b].append(a)
    
    res = set()
    for k in graph:
        if not k.startswith('t'):
            continue
        nodes = graph[k]
        pairs = set()
        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)):
                if nodes[j] in graph[nodes[i]]:
                    pairs.add((nodes[i], nodes[j]))
        
        for a, b in pairs:
            res.add(tuple(sorted([a, b, k])))
    
    return len(res)

    


def solve2():
    graph = collections.defaultdict(set)
    with open(filename) as file:
        data = file.read().splitlines()
        for line in data:
            a, b = line.split('-')
            graph[a].add(b)
            graph[b].add(a)

    def find_common(nodes):
        res = graph[nodes[0]]
        for n in nodes[1:]:
            res = res.intersection(graph[n])
        return res
    
    anslen, ans = 0, None
    visited = set()
    for k in graph:
        print(k)
        visited.add(k)
        q = {(k,)}
        while q:
            nodes = q.pop()
            common = find_common(nodes)
            for c in common:
                if c in visited:
                    continue
                new_nodes = tuple(sorted(list(nodes) + [c]))
                if new_nodes in q:
                    continue
                if len(new_nodes) > anslen:
                    anslen = len(new_nodes)
                    ans = new_nodes
                q.add(new_nodes)
    
    return ",".join(list(sorted(ans)))


print(f"First part: {solve()}")
print(f"Second part: {solve2()}")
