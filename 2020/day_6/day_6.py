with open('day_6/day_6.txt') as file:
    data = file.read()

A = [lst.split('\n') for lst in data.split('\n\n')]
# print(A)


def part_one():
    res = 0
    for group in A:
        cnt = 0
        s = set()
        for p in group:
            for c in p:
                s.add(c)
        res += len(s)
    return res
print(part_one())

import collections
def part_two():
    res = 0
    for group in A:
        cnt = collections.defaultdict(int)
        for p in group:
            p = set(p)
            for c in p:
                cnt[c] += 1
        s = sum(v == len(group) for k, v in cnt.items())
        res += s
    return res

print(part_two())

