from functools import cache

def blink(arr):
    n = len(arr)
    temp = []
    for i in range(n):
        str_form = str(arr[i])
        if arr[i] == 0:
            temp.append(1)
        elif len(str_form) % 2 == 0:
            mid = len(str_form) // 2
            left = str_form[:mid]
            right = str_form[mid:]
            left, right = int(left), int(right)

            temp.append(left)
            temp.append(right)

        else:
            temp.append(arr[i] * 2024)
    return temp


def f(arr):
    for _ in range(25):
        arr = blink(arr)

    return len(arr)


def f2(arr):

    @cache
    def solve(x, step):
        if step == 0:
            return 1
        elif x == 0:
            return solve(1, step - 1)
        elif len(str(x)) % 2 == 0:
            str_form = str(x)
            mid = len(str_form) // 2
            left = str_form[:mid]
            right = str_form[mid:]
            left, right = int(left), int(right)

            return solve(left, step - 1) + solve(right, step - 1)
        else:
            return solve(2024 * x, step - 1)

    total = 0
    for i, v in enumerate(arr):
        total += solve(v, 75)

    return total


with open('./input.txt') as file:
    data = file.read().strip()


arr = []
data = data.strip()
arr = list(map(int, data.split()))
print(f(arr))
print(f2(arr))
