import sys
import collections
import functools
import heapq
import os

filename = 'test.txt' if len(sys.argv) < 2 else 'input.txt'


def solve():
    with open(filename, 'r') as file:
        codes = [line.strip() for line in file.readlines()]
    
    grid1 = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']]
    grid2 = [[None, '^', 'A'], ['<', 'v', '>']]
    rdir = {-1: '^', 1: 'v'}
    cdir = {-1: '<', 1: '>'}
    pos1 = {}
    pos2 = {}

    for i, row in enumerate(grid1):
        for j, col in enumerate(row):
            if col is not None:
                pos1[str(col)] = (i, j)
    
    for i, row in enumerate(grid2):
        for j, col in enumerate(row):
            if col is not None:
                pos2[str(col)] = (i, j)
    res = 0
    for code in codes:
        instr = set()
        r, c = pos1['A']
        for ch in code:
            nr, nc = pos1[ch]
            rd, cd = nr - r, nc - c
            p = []

            if rd and not cd:
                p.append(rdir[rd//abs(rd)] * abs(rd))
            elif cd and not rd:
                p.append(cdir[cd//abs(cd)] * abs(cd))
            else:
                if not (c == 0 and nr == 3):
                    p.append(rdir[rd//abs(rd)] * abs(rd) + cdir[cd//abs(cd)] * abs(cd))
                if not (r == 3 and nc == 0):
                    p.append(cdir[cd//abs(cd)] * abs(cd) + rdir[rd//abs(rd)] * abs(rd))
            
            if not instr:
                for i in p:
                    instr.add(i+'A')
            else:
                temp = set()
                for inst in instr:
                    for i in p:
                        temp.add(inst + i + 'A')
                instr = temp

            r, c = nr, nc

        instr2 = set()
        for inst in instr:
            intemp = set()
            r, c = pos2['A']
            for ch in inst:
                nr, nc = pos2[ch]
                rd, cd = nr - r, nc - c
                p = []
                if rd == 0 and cd == 0:
                    p.append('A')
                elif rd and not cd:
                    p.append(rdir[rd//abs(rd)] * abs(rd) + 'A')
                elif cd and not rd:
                    p.append(cdir[cd//abs(cd)] * abs(cd) + 'A')
                else:
                    if not (c == 0 and nr == 3):
                        p.append(rdir[rd//abs(rd)] * abs(rd) + cdir[cd//abs(cd)] * abs(cd) + 'A')
                    if not (r == 3 and nc == 0):
                        p.append(cdir[cd//abs(cd)] * abs(cd) + rdir[rd//abs(rd)] * abs(rd) + 'A')
                
                if not intemp:
                    for i in p:
                        intemp.add(i)
                else:
                    temp = set()
                    for inst in intemp:
                        for i in p:
                            temp.add(inst + i)
                    intemp = temp

                r, c = nr, nc
            instr2.update(intemp)

        instr3 = set()
        for inst in instr2:
            intemp = set()
            r, c = pos2['A']
            for ch in inst:
                nr, nc = pos2[ch]
                rd, cd = nr - r, nc - c
                p = []
                if rd == 0 and cd == 0:
                    p.append('A')
                elif rd and not cd:
                    p.append(rdir[rd//abs(rd)] * abs(rd) + 'A')
                elif cd and not rd:
                    p.append(cdir[cd//abs(cd)] * abs(cd) + 'A')
                else:
                    if not (c == 0 and nr == 3):
                        p.append(rdir[rd//abs(rd)] * abs(rd) + cdir[cd//abs(cd)] * abs(cd) + 'A')
                    if not (r == 3 and nc == 0):
                        p.append(cdir[cd//abs(cd)] * abs(cd) + rdir[rd//abs(rd)] * abs(rd) + 'A')
                
                if not intemp:
                    for i in p:
                        intemp.add(i)
                else:
                    temp = set()
                    for inst in intemp:
                        for i in p:
                            temp.add(inst + i)
                    intemp = temp

                r, c = nr, nc
            instr3.update(intemp)

        min_len = min([len(i) for i in instr3])

        code = code.rstrip('A')
        code = code.lstrip('0')

        res += min_len * int(code)

    return res 

def solve2():
    with open(filename, 'r') as file:
        codes = [line.strip() for line in file.readlines()]
    
    res = 0
    rcount = 25

    grid1 = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']]
    grid2 = [[None, '^', 'A'], ['<', 'v', '>']]
    rdir = {-1: '^', 1: 'v'}
    cdir = {-1: '<', 1: '>'}
    pos1 = {}
    pos2 = {}

    for i, row in enumerate(grid1):
        for j, col in enumerate(row):
            if col is not None:
                pos1[str(col)] = (i, j)
    
    for i, row in enumerate(grid2):
        for j, col in enumerate(row):
            if col is not None:
                pos2[str(col)] = (i, j)

    @functools.lru_cache(None)
    def dfs(f, t, robot, numeric=False):
        paths = []
        if numeric:
            r, c = pos1[f]
            nr, nc = pos1[t]
            rd, cd = nr - r, nc - c
            xr, xc = '', ''
            if rd != 0:
                xr = rdir[rd//abs(rd)] * abs(rd)
            if cd != 0:
                xc = cdir[cd//abs(cd)] * abs(cd)
            if xr and xc:
                if not (c == 0 and nr == 3):
                    paths.append(xr+xc+'A')
                if not (r == 3 and nc == 0):
                    paths.append(xc+xr+'A')
            else:
                paths.append(xr+xc+'A')
            
        else:
            r, c = pos2[f]
            nr, nc = pos2[t]
            rd, cd = nr - r, nc - c
            xr, xc = '', ''
            if rd != 0:
                xr = rdir[rd//abs(rd)] * abs(rd)
            if cd != 0:
                xc = cdir[cd//abs(cd)] * abs(cd)
            if xr and xc:
                if not (c == 0 and nr == 0):
                    paths.append(xr+xc+'A')
                if not (r == 0 and nc == 0):
                    paths.append(xc+xr+'A')
            else:
                paths.append(xr+xc+'A')

        if robot == 0:
            return abs(rd) + abs(cd) + 1
        mincost = float('inf')
        for path in paths:
            cost = 0
            for i in range(len(path)):
                if i == 0:
                    cost += dfs('A', path[i], robot-1)
                else:
                    cost += dfs(path[i-1], path[i], robot-1)

            mincost = min(mincost, cost)
        
        return mincost

    for code in codes:
        cost = 0
        for i in range(len(code)):
            if i == 0:
                cost += dfs('A', code[i], rcount, True)
            else:
                cost += dfs(code[i-1], code[i], rcount, True)

        code = code.rstrip('A')
        code = code.lstrip('0')
        res += cost * int(code)
    
    return res

print(f"First part: {solve()}")
print(f"Second part: {solve2()}")
