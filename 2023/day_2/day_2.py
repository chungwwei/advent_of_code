def f(arr):
    res = 0
    for i, game in enumerate(arr):
        r = g = b = 0
        for _, s in enumerate(game):
            draws = s.split(',')
            for d in draws:
                d = d.strip()
                if "blue" in d:
                    b = max(b, int(d.split(' ')[0]))
                elif "green" in d:
                    g = max(g, int(d.split(' ')[0]))
                elif "red" in d:
                    r = max(r, int(d.split(' ')[0]))
        if r <= 12 and g <= 13 and b <= 14:
            res += i + 1
    return res
            


def f2(A):
    res = 0
    for i, game in enumerate(arr):
        r = g = b = 0
        for _, s in enumerate(game):
            draws = s.split(',')
            for d in draws:
                d = d.strip()
                if "blue" in d:
                    b = max(b, int(d.split(' ')[0]))
                elif "green" in d:
                    g = max(g, int(d.split(' ')[0]))
                elif "red" in d:
                    r = max(r, int(d.split(' ')[0]))
        res += r * g * b
    return res

with open('./part_1.txt') as file:
    data = file.read()

A = data.split('\n')
arr = []
for i, line in enumerate(A):
    rounds = line.split(':')[-1]
    sets = rounds.split(';')
    sets = [s.strip() for s in sets]
    arr.append(sets)

print(f(arr))
print(f2(arr))