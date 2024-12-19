import sys
import collections
import functools
import heapq


filename = 'test.txt' if len(sys.argv) < 2 else 'input.txt'


def solve():
    with open(filename) as file:
        a, d = file.read().split('\n\n')
    a = a.split(', ')
    d = d.split('\n')
    
    @functools.cache
    def dp(i, towel):
        p = 0
        for tw in a:
            if towel[i:].startswith(tw):
                p = max(p, dp(i+len(tw), towel)) if i+len(tw) < len(towel) else 1
        
        return p

    res = 0
    for towel in d:
        res += dp(0, towel) # brwwrr
    
    return res


def solve2():
    with open(filename) as file:
        a, d = file.read().split('\n\n')
    a = a.split(', ')
    d = d.split('\n')
    
    @functools.cache
    def dp(i, towel):
        p = 0
        for tw in a:
            if towel[i:].startswith(tw):
                p += dp(i+len(tw), towel) if i+len(tw) < len(towel) else 1
        
        return p

    res = 0
    for towel in d:
        res += dp(0, towel)
    
    return res


print(f"First part: {solve()}")
print(f"Second part: {solve2()}")
