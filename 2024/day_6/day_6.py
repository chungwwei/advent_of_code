from collections import defaultdict

def get_start(matrix):
    R, C = len(matrix), len(matrix[0])
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == '^':
                return (i, j)
    return (-1, -1)

def f(matrix):
    R, C = len(matrix), len(matrix[0])
    si, sj = get_start(matrix)
    i, j = si, sj

    seen = set()
    seen.add((i, j))

    dir = 0
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    seen = set()
    while 1:
        seen.add((i, j))

        ni = i + directions[dir][0]
        nj = j + directions[dir][1]

        if not 0 <= ni < R or not 0 <= nj < C:
            break

        if matrix[ni][nj] == "#":
            dir = (dir + 1) % 4
        else:
            i, j = ni, nj

    return len(seen)

def has_loop(matrix, si, sj, x, y):
    R, C = len(matrix), len(matrix[0])
    si, sj = get_start(matrix)
    i, j = si, sj

    seen = set()
    dir = 0
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    seen = set()
    while 1:
        if (i, j, dir) in seen:
            return True
        seen.add((i, j, dir))
        ni = i + directions[dir][0]
        nj = j + directions[dir][1]

        if not 0 <= ni < R or not 0 <= nj < C:
            return False

        if matrix[ni][nj] == "#":
            dir = (dir + 1) % 4
        else:
            i, j = ni, nj

    return len(seen)

def f2(matrix):
    R, C = len(matrix), len(matrix[0])
    si, sj = get_start(matrix)
    cnt = 0
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == '.':
                matrix[i][j] = '#'
                if has_loop(matrix, si, sj, i, j):
                    cnt += 1
                matrix[i][j] = '.'
    return cnt

with open('./input.txt') as file:
    data = file.read().strip()


lines = data.split('\n')
matrix = []
for line in lines:
    matrix.append(list(line))

matrix = matrix
print(f(matrix))
print(f2(matrix))
