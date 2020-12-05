with open('day_5/day_5.txt') as file:
    data = file.read()

A = [string for string in data.split('\n')]
# print(A)
ids = []

def compute(s):

    lo, hi = 0, 127
    row = 0
    for i in range(0, 7, 1):
        if s[i] == 'F':
            hi = (lo + hi) // 2
            row = lo
        elif s[i] == 'B':
            lo = (lo + hi + 1) // 2
            row = hi
    start, end = 0, 7
    col = 0
    for i in range(7, 10, 1):
        if s[i] == 'L':
            end = (start + end) // 2
            col= start
        elif s[i] == 'R':
            start = (start + end + 1) // 2
            col = end


    return (row) * 8 + col

def part_one():
    res = 0
    for s in A:
        cand = compute(s)
        ids.append(cand)
        res = max(cand, res)
    return res

print(part_one())
'''
BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
'''
# print(compute('BFFFBBFRRR'))
# print(compute('FFFBBBFRRR:'))
# print(compute('BBFFBBFRLL'))


def part_two():
    for i in range(100, 796, 1):
        if i not in ids:
            return i

print(part_two())


