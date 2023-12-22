import sys
from tqdm import tqdm


filename = '/home/coder/aoc/2023/example.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()
    lines = content.split('\n')
    

def solution():
    bricks = []
    for line in lines:
        f, s = line.split('~')
        x1, y1, z1, x2, y2, z2 = *map(int, f.split(',')), *map(int, s.split(','))
        z1, z2 = min(z1, z2), max(z1, z2)
        bricks.append((x1, y1, z1, x2, y2, z2))

    bricks = sorted(bricks, key=lambda b: (b[2]))

    def free_falling(bricks, skip=-1):
        res = {}
        for i in range(len(bricks)):
            if i == skip:
                continue
            x1, y1, z1, x2, y2, z2 = bricks[i]
            height, hpz2 = z2-z1, 0
            for j in res:
                px1, py1, pz1, px2, py2, pz2 = res[j]
                if pz2 <= hpz2:
                    continue
                if ((x1 <= px1 <= x2 or x1 <= px2 <= x2) or (px1 <= x1 <= px2 or px1 <= x2 <= px2)) and ((y1 <= py1 <= y2 or y1 <= py2 <= y2) or (py1 <= y1 <= py2 or py1 <= y2 <= py2)):
                    if pz2 > hpz2:
                        hpz2 = pz2
            if hpz2:
                z1, z2 = hpz2+1, hpz2+1+height
                res[i] = (x1, y1, z1, x2, y2, z2)
            else:
                res[i] = (x1, y1, 1, x2, y2, height+1)
        return res
    

    bricks_dict = free_falling(bricks)
    res, part2 = 0, 0
    for i in tqdm(range(len(bricks))):
        d = free_falling(bricks, i)
        diff = 0
        for j in d:
            if d[j] != bricks_dict[j]:
                diff += 1
        
        part2 += diff
        if not diff:
            res += 1

    return res, part2
            

for part2 in [False]:
    print(solution())