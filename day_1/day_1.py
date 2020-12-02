with open('day_1.txt') as file:
    data = file.read()

A = [int(n) for n in data.split('\n')[:-1]]
n = len(A)
# for i in range(len(A)):
#     for j in range(i + 1, len(A)):
#         if A[i] + A[j] == 2020:
#             print(A[i] * A[j])

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if A[i] + A[j] + A[k] == 2020:
                print(A[i] * A[j] * A[k])


