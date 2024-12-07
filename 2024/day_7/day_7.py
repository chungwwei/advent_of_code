def valid(arr, k):
    n = len(arr)
    def dfs(i, s):
        if i == n:
            return s == k
        plus = dfs(i + 1, s + arr[i])
        mult = dfs(i + 1, s * arr[i])

        return plus or mult

    return dfs(1, arr[0])

def f(tests):
    total = 0
    for test in tests:
        if valid(test[0], test[1]):
            total += test[1]
    return total


def valid2(arr, k):
    n = len(arr)
    def dfs(i, s):
        if i == n:
            return s == k
        plus = dfs(i + 1, s + arr[i])
        mult = dfs(i + 1, s * arr[i])
        temp = str(s) + str(arr[i])
        temp = int(temp)
        concat = dfs(i + 1, temp)

        return plus or mult or concat

    return dfs(1, arr[0])



def f2(matrix):
    total = 0
    for test in tests:
        if valid2(test[0], test[1]):
            total += test[1]
    return total


with open('./input.txt') as file:
    data = file.read().strip()


lines = data.split('\n')
tests = []
for line in lines:
    result, arr = line.split(':')
    result = int(result)
    arr = list(map(int, arr.split()))
    tests.append((arr, result))


print(f(tests))
print(f2(tests))
