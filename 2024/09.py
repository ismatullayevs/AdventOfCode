import sys
from collections import defaultdict

filename = 'test.txt' if len(sys.argv) < 2 else 'input.txt'

def solve():
    with open(filename) as f:
        nums = f.read()
        res = 0
        s = []
        for i in range(len(nums)):
            if i % 2 == 0:
                s += [i//2] * int(nums[i])
            else:
                s += [None] * int(nums[i])
        
        l, r = 0, len(s)-1
        while l <= r:
            if s[l] is None:
                while s[r] is None:
                    r -= 1
                if r < l:
                    break
                res += l * int(s[r])
                r -= 1
            else:
                res += l * int(s[l])
            l += 1
        return res

def solve2():
    with open(filename) as f:
        nums = f.read()
        res = 0
        s = []
        vv = {}
        spos = {}
        gaps = defaultdict(int)
        for i in range(len(nums)):
            if i % 2 == 0:
                spos[i//2] = len(s)
                s += [i//2] * int(nums[i])
                vv[i//2] = int(nums[i])
            else:
                gaps[len(s)+int(nums[i])] = int(nums[i])
                s += [None] * int(nums[i])
        
        for i in range(len(vv)-1, 0, -1):
            for k, v in gaps.items():
                if k-v >= spos[i]:
                    break
                if vv[i] <= v:
                    s[k-v:k-v+vv[i]] = [i] * vv[i]
                    s[spos[i]:spos[i]+vv[i]] = [None] * vv[i]
                    gaps[k] = v - vv[i]
                    break
        
        res = 0
        for i in range(len(s)):
            if s[i] is not None:
                res += i * s[i]
        
        return res


print(f"First part: {solve()}")
print(f"Second part: {solve2()}")