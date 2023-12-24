import sys
import z3


filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()
    lines = content.split('\n')


def part_one():
    funcs, start, end = [], 200000000000000, 400000000000000
    for line in lines:
        pos, vel = line.split(' @ ')
        px, py, _ = [int(point) for point in pos.split(', ')]
        vx, vy, _ = [int(vel) for vel in vel.split(', ')]
        slope = vy / vx
        intercept = py - slope * px
        dir = int.__lt__ if vx < 0 else int.__gt__
        funcs.append((slope, intercept, px, dir))
        
    res = 0
    for i in range(len(funcs)):
        cx, cy, scx, scdir = funcs[i]
        for j in range(i + 1, len(funcs)):
            dx, dy, sdx, sddir = funcs[j]
            if cx == dx:
                if cy == dy:
                    res += 1
                continue
            x = (dy - cy) / (cx - dx)
            y = cx * x + cy
            
            # check if they only cross in the future
            if not scdir(int(x), int(scx)) or not sddir(int(x), int(sdx)):
                continue
            
            if start <= x <= end and start <= y <= end:
                res += 1

    return res


def part_two():
    hails = {}
    for line in lines:
        pos, vel = line.split(' @ ')
        px, py, pz = [float(point) for point in pos.split(', ')]
        vx, vy, vz = [float(vel) for vel in vel.split(', ')]
        hails[(px, py, pz)] = (vx, vy, vz)
    
    x, y, z, vx, vy, vz = z3.Reals('x y z vx vy vz')
    s = z3.Solver()

    for (px, py, pz), (pvx, pvy, pvz) in hails.items():
        t = z3.Real(f"t_{(px, py, pz)}")
        s.add(px + pvx * t == x + vx * t)
        s.add(py + pvy * t == y + vy * t)
        s.add(pz + pvz * t == z + vz * t)
    
    s.check()
    m = s.model()
    return eval(str(m[x] + m[y] + m[z]))
        

print(part_one())
print(part_two())