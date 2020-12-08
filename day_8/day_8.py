with open('day_8/day_8.txt') as file:
    data = file.read()

A = [n.split() for n in data.split('\n')]
n = len(A)

def part_one(A):
    acc = 0
    seen = set()
    i = 0
    while i < len(A) and i not in seen:
        ins = A[i]
        code, num = ins[0], ins[1]
        seen.add(i)
        if code == 'acc':
            acc += int(num)
            i += 1
        elif code == 'nop':
            i += 1
        elif code == 'jmp':
            i += int(num)
    terminate = i == len(A)
    return terminate, acc


import copy
def part_two(A):

    for i, ins in enumerate(A):
        code, num = ins[0], ins[1] 
        if code == 'nop' or code == 'jmp':
            temp = copy.deepcopy(A)
            temp[i][0] = 'jmp' if code == 'nop' else 'nop'

            terminated, acc = part_one(temp)
            if terminated:
                return acc
    return 0
print(part_two(A))