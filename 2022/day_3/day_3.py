def common(first, second):
    for i in range(len(first)):
        for j in range(len(second)):
            if first[i] == second[j]:
                return first[i]
    return None


def f(A):
    res = 0
    for rucksack in A:
        n = len(rucksack)
        half = n // 2
        first = rucksack[: half]
        second = rucksack[half:]
        c = common(first, second)
        if c.islower():
            res += ord(c) - ord('a') + 1
        else:
            res += ord(c) - ord('A') + 26 + 1

    return res


def common2(lsts):
    common = set(lsts[0])
    for lst in lsts:
        n_set = set()
        for c in lst:
            if c in common:
                n_set.add(c)
        common = n_set
    return list(common).pop()



def f2(A):
    res = 0
    for i in range(0, len(A), 3):
        one = A[i]
        two = A[i + 1]
        three = A[i + 2]
        c = common2([one, two, three])
        if c.islower():
            res += ord(c) - ord('a') + 1
        else:
            res += ord(c) - ord('A') + 26 + 1
    return res


with open('./day_3.txt') as file:
    data = file.read()

A = data.split('\n')
print(f(A))
print(f2(A))