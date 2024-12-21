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
    return res

print(f"First part: {solve()}")
print(f"Second part: {solve2()}")
