import sys
from collections import deque


filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()
    lines = content.splitlines()


def solution(part2):
    modules = {'button': ['broadcaster']}
    states = {}
    for line in lines:
        src, dst = line.split(' -> ')
        dst = dst.split(', ')
        modules[src] = dst
        if src[0] == '%':
            states[src] = 0
        elif src[0] == '&':
            states[src] = {}

    for module, dsts in modules.items():
        new_dsts = []
        for dst in dsts:
            if '&'+dst in modules:
                new_dsts.append('&'+dst)
                states['&'+dst][module] = 0
            elif '%'+dst in modules:
                new_dsts.append('%'+dst)
            else:
                new_dsts.append(dst)
        modules[module] = new_dsts


    t, low, high = 0, 0, 0
    cycles = []
    while True:
        q = deque(((None, 'button', 0),))
        while q:
            prev, src, level = q.popleft()
            if src not in modules:
                continue

            send_level = 0
            dsts = modules[src]
            if src[0] == '%':
                if level == 1:
                    continue
                states[src] = 0 if states[src] else 1
                send_level = states[src]
            elif src[0] == '&':
                states[src][prev] = level
                if all(states[src].values()):
                    send_level = 0
                else:
                    send_level = 1
            
            for dst in dsts:
                q.append((src, dst, send_level))
                # print(f'From {src} sent a {"high" if send_level else "low"} level pulse to {dst}')
                if send_level == 0:
                    low += 1
                else:
                    high += 1

                if part2:
                    if dst == '&bq' and send_level == 1:
                        cycles.append(t+1)
                        if len(cycles) == 4: 
                            return cycles[0]*cycles[1]*cycles[2]*cycles[3]
        t += 1
        if t == 1000 and not part2:
            break
        
    return low * high


for part2 in [False, True]:
    print(f"Part {'two' if part2 else 'one'}: {solution(part2)}")
