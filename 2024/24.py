import sys
import collections
import functools
import heapq

filename = 'test.txt' if len(sys.argv) < 2 else 'input.txt'


def solve():
    with open(filename) as file:
        init, gates = file.read().strip().split('\n\n')
    init = [x.split(': ') for x in init.split('\n')]
    gates = [x.split(' -> ') for x in gates.split('\n')]
    op = {'AND': lambda x, y: x & y,
          'OR': lambda x, y: x | y,
          'XOR': lambda x, y: x ^ y,
    }

    values = {}
    for k, v in init:
        values[k] = int(v)

    graph = {}
    lim = 0
    for gate in gates:
        l, g, r = gate[0].split(' ')
        res = gate[1]
        if res.startswith('z'):
            lim = max(lim, int(res[1:]))
        graph[gate[1]] = (l, r, g)
    
    def dfs(node):
        if node in values:
            return values[node]
        
        l, r, g = graph[node]
        lval = dfs(l)
        rval = dfs(r)
        val = op[g](lval, rval)
        values[node] = val

        return val

    res = []
    for i in range(lim+1):
        k = 'z' + f'{i}'.rjust(2, '0')
        res.append(dfs(k))

    res_bin = ''.join(str(x) for x in res[::-1])
    return int(res_bin, 2)


def solve2():
    gates = {}
    with open(filename) as file:
        for line in file:
            if '->' in line:
                k, v = line.strip().split(' -> ')
                l, op, r = k.split(' ')
                gates[v] = (l, r, op)


    def rjust(s, n):
        return s + str(n).rjust(2, '0')


    def is_xor(wire, num):
        l, r, op = gates[wire]
        if op != 'XOR':
            return False
        
        return sorted([l, r]) == [rjust('x', num), rjust('y', num)]


    def is_direct_carry(wire, num):
        l, r, op = gates[wire]
        if op != 'AND': return False
        return sorted([l, r]) == [rjust('x', num), rjust('y', num)]


    def is_indirect_carry(wire, num):
        l, r, op = gates[wire]
        if op != 'AND': return False
        return is_xor(l, num) and is_carry(r, num) or is_xor(r, num) and is_carry(l, num)


    def is_carry(wire, num):
        l, r, op = gates[wire]
        if num == 1:
            if op != 'AND': return False
            return sorted([l, r]) == [rjust('x', 0), rjust('y', 0)]
        
        if op != 'OR': return False
        return is_direct_carry(l, num-1) and is_indirect_carry(r, num-1) or is_direct_carry(r, num-1) and is_indirect_carry(l, num-1)


    def is_valid(num):
        gate = rjust('z', num)
        l, r, op = gates[gate]
        if op != 'XOR':
            return False
        
        if num == 0:
            return is_xor(gate, num)
        
        return is_xor(l, num) and is_carry(r, num) or is_xor(r, num) and is_carry(l, num)

    for i in range(45):
        if not is_valid(i):
            print(f'{rjust("z", i)} is invalid')
            break
        
        # correct each z manually until all z are correct

print(f"First part: {solve()}")
print(f"Second part: {solve2()}")
