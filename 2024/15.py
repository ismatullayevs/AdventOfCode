import sys
import collections
import functools

filename = 'test.txt' if len(sys.argv) < 2 else 'input.txt'


def solve():
    with open(filename, 'r') as f:
        content = f.read().strip()
        mx, ds = content.split('\n\n')
    mx = mx.split('\n')
    mx = [list(s) for s in mx]
    ds = list(ds)
    R, C = len(mx), len(mx[0])
    r, c = 0, 0
    for i in range(R):
        for j in range(C):
            if mx[i][j] == '@':
                r, c = i, j
                break
    
    dirs = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
    for d in ds:
        if d == '\n': continue
        dr, dc = dirs[d]
        er, ec = r, c
        while mx[er+dr][ec+dc] == 'O':
            er += dr
            ec += dc
        if mx[er+dr][ec+dc] == '#':
            continue
        r += dr
        c += dc
        er += dr
        ec += dc
        mx[er][ec] = mx[r][c]
        mx[r][c] = '@'
        mx[r-dr][c-dc] = '.'

    res = 0
    for i in range(R):
        for j in range(C):
            if mx[i][j] == 'O':
                res += i * 100 + j
    
    return res

def solve2():
    with open(filename, 'r') as f:
        content = f.read().strip()
        mx, ds = content.split('\n\n')
    mx = mx.split('\n')
    mx = [list(s) for s in mx]
    ds = list(ds)
    newmx = [[] for _ in range(len(mx))]
    for i in range(len(mx)):
        for j in range(len(mx[0])):
            if mx[i][j] == '@':
                newmx[i].extend(['@', '.'])
            elif mx[i][j] == 'O':
                newmx[i].extend(['[', ']'])
            else:
                newmx[i].extend([mx[i][j]] * 2)
    mx = newmx
    R, C = len(mx), len(mx[0])
    r, c = 0, 0
    for i in range(R):
        for j in range(C):
            if mx[i][j] == '@':
                r, c = i, j
                break
    # mx[r][c] = '.'
    dirs = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}

    def dfs(r, c, dr):
        boxes = [(r, c)]
        if mx[r+dr][c] == '[':
            can_move, bs = dfs(r+dr, c, dr)
            if can_move:
                boxes.extend(bs)
            else:
                return False, []
        else:
            if mx[r+dr][c] == "#" or mx[r+dr][c+1] == '#':
                return False, []
            if mx[r+dr][c] == ']':
                can_move, bs = dfs(r+dr, c-1, dr)
                if can_move:
                    boxes.extend(bs)
                else:
                    return False, []
            if mx[r+dr][c+1] == '[':
                can_move, bs = dfs(r+dr, c+1, dr)
                if can_move:
                    boxes.extend(bs)
                else:
                    return False, []
        
        return True, boxes

    for d in ds:
        if d == '\n': continue
        dr, dc = dirs[d]
        if dr == 0:
            er, ec = r, c
            while mx[er+dr][ec+dc] in ['[', ']']:
                er += dr
                ec += dc
            if mx[er+dr][ec+dc] == '#':
                continue
            er += dr
            ec += dc
            while er != r or ec != c:
                mx[er][ec] = mx[er-dr][ec-dc]
                er -= dr
                ec -= dc
            mx[r][c] = '.'
            r += dr
            c += dc
            mx[r][c] = '@'
        else:
            if mx[r+dr][c] not in ['[', ']']:
                if mx[r+dr][c] == '#':
                    continue
                mx[r+dr][c] = mx[r][c]
                mx[r][c] = '.'
                r += dr
                c += dc
                mx[r][c] = '@'
            else:
                if mx[r+dr][c] == '[':
                    can_move, boxes = dfs(r+dr, c, dr)
                else:
                    can_move, boxes = dfs(r+dr, c-1, dr)
                if can_move:
                    b = []
                    boxes.reverse()
                    for box in boxes:
                        if box not in b:
                            b.append(box)
                    boxes = b
                    for br, bc in boxes:
                        mx[br+dr][bc] = mx[br][bc]
                        mx[br+dr][bc+1] = mx[br][bc+1]
                        mx[br][bc] = '.'
                        mx[br][bc+1] = '.'
                    mx[r][c] = '.'
                    r += dr
                    c += dc
                    mx[r][c] = '@'
                else:
                    continue

        # import time
        # time.sleep(.1)
        # import os
        # os.system('clear')
        # print("\n".join("".join(s) for s in mx))
    
    res = 0
    for i in range(len(mx)):
        for j in range(len(mx[0])):
            if mx[i][j] == '[':
                res += i * 100 + j
    return res

print(f"First part: {solve()}")
print(f"Second part: {solve2()}")
