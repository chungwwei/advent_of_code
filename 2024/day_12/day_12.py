from collections import deque

# def get_area(matrix):
#     R, C = len(matrix), len(matrix[0])

#     def dfs(i, j, plant):
#         if not 0 <= i < R:
#             return 0
#         if not 0 <= j < C:
#             return 0
#         if matrix[i][j] != plant:
#             return 0

#         matrix[i][j] = "#"
#         a = dfs(i + 1, j, plant)
#         b = dfs(i - 1, j, plant)
#         c = dfs(i, j - 1, plant)
#         d = dfs(i, j + 1, plant)

#         return 1 + a + b + c + d


#     cnt = defaultdict(int)
#     for i in range(R):
#         for j in range(C):
#             if matrix[i][j] != '#':
#                 a = dfs(i, j, matrix[i][j])
#                 cnt[(i, j)] = a
#     return cnt

def f(G):
    R, C = len(matrix), len(matrix[0])
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    seen = set()
    total = 0
    for i in range(R):
        for j in range(C):
            if (i, j) in seen:
                continue
            q = deque([(i, j)])
            area = 0
            perimeter = 0
            while q:
                x, y = q.popleft()
                if (x, y) in seen:
                    continue
                seen.add((x, y))
                area += 1
                for di, dj in dirs:
                    ni, nj = x + di, y + dj
                    if 0<= ni < R and 0 <= nj < C and matrix[ni][nj] == matrix[x][y]:
                        q.append((ni, nj))
                    else:
                        perimeter += 1
            total += area * perimeter
    return total

def f2(matrix):
    pass


with open('./input.txt') as file:
    data = file.read().strip()


matrix = []
lines = data.split("\n")
for line in lines:
    matrix.append(list(line))
print(f(matrix))
print(f2(matrix))
