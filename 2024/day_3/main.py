import re


def f(arr):
    total = 0
    for _, (x, y) in enumerate(arr):
        total += int(x) * int(y)
    return total


def f2(arr):
    enabled = True
    total = 0
    for a in arr:
        if a == 'enables':
            enabled = True
        elif a == 'disables':
            enabled = False
        else:
            total += a[0] * a[1] if enabled else 0
    return total


with open('./input.txt') as file:
    data = file.read()


lines = data.split('\n')
arr = []
pattern = r"mul\((\d{1,3}),\s?(\d{1,3})\)"
pattern2 = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
instructions = re.findall(pattern2, "".join(data))
for inst in instructions:
    match inst[0]:
        case "do()":
            arr.append("enables")
        case "don't()":
            arr.append("disables")
        case _:
            # arr.append((int(inst[0]), int(inst[1])))
            arr.append((int(inst[1]), int(inst[2])))


#print(f(arr))
print(f2(arr))
