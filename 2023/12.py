import sys


filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()
    lines = content.split('\n')


def part_one():
    pass


def part_two():
    pass


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")
