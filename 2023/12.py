import sys
from functools import lru_cache


filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()
    lines = content.split('\n')


def solution(part2):
    valid = lambda springs, start, end: False if start < 1 or end >= len(springs) or "#" in springs[:start] or springs[end:] == '#' or '.' in springs[start:end] else True

    @lru_cache
    def dfs(springs, nums):
        if not nums:
            return 0 if '#' in springs else 1

        total = 0
        for start in range(len(springs)-nums[0]):
            end = start + nums[0]
            if valid(springs, start, end):
                total += dfs(springs[end:], nums[1:])

        return total

    total = 0
    for line in lines:
        springs, nums = line.split(' ')
        nums = tuple(int(num) for num in nums.split(','))
        if part2: springs, nums = '?'.join(spring for spring in [springs] * 5), nums * 5
        total += dfs(f".{springs}.", nums)

    return total


for part2 in [False, True]:
    print(f"Part {'two' if part2 else 'one'}: {solution(part2)}")
