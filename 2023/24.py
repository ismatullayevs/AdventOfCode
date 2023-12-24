import sys
from tqdm import tqdm


filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()
    lines = content.split('\n')


def part_one():
    funcs, start, end = [], 200000000000000, 400000000000000
    for line in lines:
        points, velocity = line.split(' @ ')
        px, py, pz = [int(point) for point in points.split(', ')]
        vx, vy, vz = [int(vel) for vel in velocity.split(', ')]
        slope = vy / vx
        intercept = py - slope * px
        dir = int.__lt__ if vx < 0 else int.__gt__
        funcs.append((slope, intercept, px, dir))
        
    res = 0
    for i in tqdm(range(len(funcs))):
        cx, cy, scx, scdir = funcs[i]
        for j in range(i + 1, len(funcs)):
            dx, dy, sdx, sddir = funcs[j]
            if cx == dx:
                if cy == dy:
                    res += 1
                continue
            x = (dy - cy) / (cx - dx)
            y = cx * x + cy
            
            # check if they don't cross before the snowing
            if not scdir(int(x), int(scx)) or not sddir(int(x), int(sdx)):
                continue
            
            if start <= x <= end and start <= y <= end:
                res += 1

    return res


def part_two():
    pass


print(part_one())
print(part_two())