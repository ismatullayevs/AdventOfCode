import sys


filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()


def solution(part2):
    workflows, parts = content.split('\n\n')
    workflows, parts = workflows.split('\n'), parts.split('\n')

    W = {}
    for workflow in workflows:
        name, rules = workflow.strip('}').split('{')
        rules = [rule for rule in rules.split(',')]
        r = []
        for rule in rules:
            rule = rule.split(':')
            if len(rule) == 2:
                exp, des = rule
                if '<' in exp:
                    a, b = exp.split('<')
                    r.append((a, int(b), int.__lt__, des))
                else:
                    a, b = exp.split('>')
                    r.append((a, int(b), int.__gt__, des))
            else:
                r.append((None, None, None, rule[0]))
        W[name] = r

    if part2:
        curr_rules = []
        reverse = {int.__gt__: int.__le__, int.__lt__: int.__ge__}

        def calc_possibilities(curr_rules):
            total = 1
            for ch in 'asxm':
                start, end = 1, 4000
                for a, val, op in curr_rules:
                    if a != ch:
                        continue
                    if op == int.__gt__:
                        start = max(start, val + 1)
                    elif op == int.__lt__:
                        end = min(end, val - 1)
                    elif op == int.__ge__:
                        start = max(start, val)
                    elif op == int.__le__:
                        end = min(end, val)
                total *= end - start + 1
            return total

        def dfs(curr_rules, curr):
            rules = W[curr]
            total = 0
            for a, val, op, des in rules:
                cr = curr_rules.copy()
                if a:
                    cr.append((a, val, op))
                    curr_rules.append((a, val, reverse[op]))

                if des == 'A':
                    total += calc_possibilities(cr)
                    continue
                if des == 'R':
                    continue

                total += dfs(cr, des)

            return total

        return dfs(curr_rules, 'in')

    total = 0
    for part in parts:
        c = part[1:-1].split(',')
        c = {k: v for k, v in [x.split('=') for x in c]}
        curr = 'in'
        while True:
            loopbreak = False
            rules = W[curr]
            for a, val, op, des in rules:
                if a is None:
                    if des == 'A':
                        total += sum(int(x) for x in c.values())
                        loopbreak = True
                        break
                    if des == 'R':
                        loopbreak = True
                        break

                    curr = des
                    break

                else:
                    if op(int(c[a]), int(val)):
                        if des == 'A':
                            total += sum(int(x) for x in c.values())
                            loopbreak = True
                            break
                        if des == 'R':
                            loopbreak = True
                            break

                        curr = des
                        break

            if loopbreak:
                break
    return total


for part2 in [False, True]:
    print(f"Part {'two' if part2 else 'one'}: {solution(part2)}")
