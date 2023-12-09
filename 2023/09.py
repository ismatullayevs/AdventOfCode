import sys


filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()
    lines = content.split('\n')


def part_one():
    def recursion(lst):
        if len(set(lst)) == 1:
            return lst[0]
        diff = []
        for i in range(1, len(lst)):
            diff.append(lst[i] - lst[i-1])
        return lst[-1] + recursion(diff)
    
    sum = 0
    for line in lines:
        sum += recursion([int(x) for x in line.split(' ')])
    return sum

def part_two():
    def recursion(lst):
        if len(set(lst)) == 1:
            return lst[0]
        diff = []
        for i in range(1, len(lst)):
            diff.append(lst[i] - lst[i-1])
        return lst[-1] + recursion(diff)
    
    sum = 0
    for line in lines:
        sum += recursion([int(x) for x in line.split(' ')[::-1]])
    return sum


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")
