with open('day_2.txt') as file:
    data = file.read()

A = [n for n in data.split('\n')]

res = 0
# for line in A:
#     parts = line.split(' ')
#     a = parts[0].split('-')
#     lo, hi = int(a[0]), int(a[1])

#     w = parts[1][0]

#     password = parts[-1]
#     cnt = password.count(w)
#     if lo <= cnt <= hi:
#         res += 1

for line in A:
    parts = line.split(' ')
    a = parts[0].split('-')
    x, y = int(a[0]), int(a[1])

    w = parts[1][0]
    password = parts[-1]

    if password[x - 1] != w and password[y - 1] == w:
        res += 1
    if password[x - 1] == w and password[y - 1] != w:
        res += 1
    
print(res)


