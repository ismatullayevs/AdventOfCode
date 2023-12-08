import sys
import math


filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()
    lines = content.split('\n')


def part_one():
    ins = lines[0].split('=')[0].strip()
    curr = 'AAA'
    map = {}
    for line in lines[2:]:
        src, dst = line.split(' = ')
        left, right = dst[1:-1].split(', ')
        map[src] = (left, right)

    moves = 0
    while curr != 'ZZZ':
        turn = ins[moves % len(ins)]
        if turn == 'L':
            curr = map[curr][0]
        else:
            curr = map[curr][1]
        moves += 1
    return moves


def part_two():
    ins = lines[0].split('=')[0].strip()
    curr = []
    map = {}
    for line in lines[2:]:
        src, dst = line.split(' = ')
        left, right = dst[1:-1].split(', ')
        map[src] = (left, right)
        if src.endswith('A'):
            curr.append(src)

    moves = 0
    intervals = {}
    while True:
        for i, pos in enumerate(curr):
            turn = ins[moves % len(ins)]
            if turn == 'L':
                next = map[pos][0]
            else:
                next = map[pos][1]
            curr[i] = next
            if next.endswith('Z'):
                intervals[i] = moves + 1
                if len(intervals) == len(curr):
                    return math.lcm(*intervals.values())
        moves += 1


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")
