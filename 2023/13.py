import sys


filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()
    lines = content.split('\n')
    

def part_one():
    games = [game.split('\n') for game in content.split('\n\n')]
    ans = 0
    for gi, game in enumerate(games):
        for i in range(len(game)-1):
            up, down, r = game[i], game[i+1], 0
            while up == down:
                r += 1
                if i+r+1 >= len(game) or i-r < 0:
                    ans += 100 * (i+1)
                    break
                up, down = game[i-r], game[i+r+1]
        
        for i in range(len(game[0])-1):
            left = [game[j][i] for j in range(len(game))]
            right = [game[j][i+1] for j in range(len(game))]
            r = 0
            
            while left == right:
                r += 1
                if i+r+1 >= len(game[0]) or i-r < 0:
                    ans += i + 1
                    break
                left = [game[j][i-r] for j in range(len(game))]
                right = [game[j][i+r+1] for j in range(len(game))]

    return ans


def part_two():
    games = [game.split('\n') for game in content.split('\n\n')]
    ans = 0
    for gi, game in enumerate(games):
        found = False
        for i in range(len(game)-1):
            smudges, r = 0, 0
            while smudges < 2:
                up, down = game[i-r], game[i+r+1]
                for j in range(len(up)):
                    if up[j] != down[j]:
                        smudges += 1
                
                r += 1
                if i+r+1 >= len(game) or i-r < 0:
                    if smudges == 1:
                        ans += 100 * (i+1)
                        found = True
                    break
            if found:
                break
        
        if found:
            continue

        for i in range(len(game[0])-1):
            smudges, r = 0, 0
            
            while smudges < 2:
                left = [game[j][i-r] for j in range(len(game))]
                right = [game[j][i+r+1] for j in range(len(game))]

                for j in range(len(left)):
                    if left[j] != right[j]:
                        smudges += 1

                r += 1
                if i+r+1 >= len(game[0]) or i-r < 0:
                    if smudges == 1:
                        ans += i + 1
                        found = True
                    break

            if found:
                break

    return ans


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")