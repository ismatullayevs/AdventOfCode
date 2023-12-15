import sys


filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()


def hash(word):
    res = 0
    for char in word:
        res += ord(char)
        res *= 17
        res %= 256
    return res
    

def part_one():
    return sum(hash(word) for word in content.split(','))


def part_two():
    boxes = [[] for _ in range(256)]

    for part in content.split(','):
        for sym in ['=', '-']:
            if not sym in part:
                continue
                
            label, num = part.split(sym)
            if sym == '=':
                h = hash(label)
                
                for i, (l, n) in enumerate(boxes[h]):
                    if l == label:
                        boxes[h][i] = (label, int(num))
                        break
                else:
                    boxes[h].append((label, int(num)))
            else:
                h = hash(label)

                for i, (l, n) in enumerate(boxes[h]):
                    if l == label:
                        boxes[h].remove((l, n))
                        break

    res = 0
    for i in range(256):
        for s, (label, num) in enumerate(boxes[i]):
            res += (i + 1) * (s + 1) * num

    return res            

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")