from collections import deque
from typing import List, Tuple

def has_path(matrix: List[List[int]], coord: Tuple[int, int]) -> int:
    q = deque([[coord[0], coord[1], '0']])
    R, C = len(matrix), len(matrix[0])
    seen = set()
    seen.add((coord[0], coord[1]))
    cnt = 0
    while q:
        i, j, height = q.popleft()
        height = int(height)
        if height == 9:
            cnt += 1
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <=ni < R and 0 <= nj < C and (ni, nj) not in seen and matrix[ni][nj] != '.' and int(matrix[ni][nj]) - 1 == height:
                q.append((ni, nj, matrix[ni][nj]))
                seen.add((ni, nj))
    return cnt

def f(matrix):
    R, C = len(matrix), len(matrix[0])
    heads = []
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == '0':
                heads.append((i, j, '0'))

    cnt = 0
    for coord in heads:
        cnt += has_path(matrix, coord)
    return cnt


def f2(matrix):
    R, C = len(matrix), len(matrix[0])
    heads = []

    def dfs(i, j, prev, seen):

        if not 0 <= i < R: return 0
        if not 0 <= j < C: return 0

        if matrix[i][j] == '.': return 0
        if int(matrix[i][j]) - 1 != int(prev): return 0

        if matrix[i][j] == '9': return 1

        seen.add((i, j))

        a = dfs(i + 1, j, matrix[i][j], seen)
        b = dfs(i - 1, j, matrix[i][j], seen)
        c = dfs(i, j - 1, matrix[i][j], seen)
        d = dfs(i, j + 1, matrix[i][j], seen)

        seen.remove((i, j))

        return a + b + c + d

    for i in range(R):
        for j in range(C):
            if matrix[i][j] == '0':
                heads.append((i, j, '0'))

    ratings = 0
    for coord in heads:
        ratings += dfs(coord[0], coord[1], -1, set())
    return ratings


with open('./input.txt') as file:
    data = file.read().strip()


matrix = []
lines = data.split('\n')
for line in lines:
    matrix.append(list(line))

print(f(matrix))
print(f2(matrix))
