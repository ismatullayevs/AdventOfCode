import sys


filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()


def part_one():
    arr = []
    for line in content.split('\n'):
        cards, bid = line.split(' ')
        arr.append((cards, int(bid)))

    def sort_cards(x):
        chars = [str(i) for i in range(2, 10)] + list('TJQKA')
        cards, _ = x
        count = {c:cards.count(c) for c in set(cards)}
        count = sorted(count.values(), reverse=True)
        return (tuple(count), tuple(chars.index(c) for c in cards))

    arr = sorted(arr, key=sort_cards)
    return sum(bid * (i + 1) for i, (_, bid) in enumerate(arr))


def part_two():
    arr = []
    for line in content.split('\n'):
        cards, bid = line.split(' ')
        arr.append((cards, int(bid)))

    def sort_cards(x):
        chars = ['J'] + [str(i) for i in range(2, 10)] + list('TQKA')
        cards, _ = x
        count, js = {c:cards.count(c) for c in set(cards) if c != 'J'}, cards.count('J')
        count = sorted(count.values(), reverse=True)
        count.append(0)
        count[0] += js
        return (tuple(count), tuple(chars.index(c) for c in cards))

    arr = sorted(arr, key=sort_cards)
    return sum(bid * (i + 1) for i, (_, bid) in enumerate(arr))


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")