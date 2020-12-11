import collections
with open('day_11/day_11.txt') as file:
    data = file.read()

A = [n for n in data.split('\n')]
n = len(A)

def adj(A, i, j, R, C):
    cnt = 0
    for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i + 1, j + 1), (i + 1, j - 1), (i - 1, j - 1), (i - 1, j + 1)]:
        if 0 <= r < R and 0 <= c < C:
            cnt += 1 if A[r][c] == '#' else 0 
    return cnt

def part_one(A):
    seen = set()
    R, C = len(A), len(A[0])
    seen.add(''.join(A))
    while True:
        B = []
        for i in range(R):
            temp = []
            for j in range(C):
                nei = adj(A, i, j, R, C) 
                if A[i][j] == 'L' and nei == 0:
                    temp.append('#')
                elif A[i][j] == '#' and nei >= 4:
                    temp.append('L')
                else:
                    temp.append(A[i][j])
            B.append(''.join(temp))
        string = ''.join(B)
        if string in seen:
            return sum(B[i][j] == '#' for j in range(C) for i in range(R))
        seen.add(string)
        A = list(B)
    return

# print(part_one(A))


# def nei_2():
#     pass

# def part_two(A):
#     seen = set()
#     R, C = len(A), len(A[0])
#     seen.add(''.join(A))
#     while True:
#         B = []
#         for i in range(R):
#             temp = []
#             for j in range(C):
#                 nei = adj(A, i, j, R, C) 
#                 if A[i][j] == 'L' and nei == 0:
#                     temp.append('#')
#                 elif A[i][j] == '#' and nei >= 5:
#                     temp.append('L')
#                 else:
#                     temp.append(A[i][j])
#             B.append(''.join(temp))
#         string = ''.join(B)
#         if string in seen:
#             return sum(B[i][j] == '#' for j in range(C) for i in range(R))
#         seen.add(string)
#         A = list(B)
#     return

# print(part_two())

