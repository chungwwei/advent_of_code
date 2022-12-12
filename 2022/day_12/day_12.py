from string import ascii_lowercase
from heapq import heappop, heappush
from collections import deque




def height(s):
    if s in ascii_lowercase:
        return ascii_lowercase.index(s)
    if s == "S":
        return 0
    if s == "E":
        return 25

def bfs(arr, R, C, start, end):
    seen = set()
    q = deque()
    q.append((start[0], start[1], 0))
    while q:
        i, j, d = q.popleft()
        if i == end[0] and j == end[1]:
            return d
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= ni < R and 0 <= nj < C and (ni, nj) not in seen and height(grid[ni][nj]) <= height(grid[i][j]) + 1:
                q.append((ni, nj, d + 1))
                seen.add((ni, nj))
    return -1
    
def multi_source(arr, R, C):
    seen = set()
    q = deque()
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'a':
                q.append((i, j, 0))
                seen.add((i, j))
    while q:
        i, j, d = q.popleft()
        if i == end[0] and j == end[1]:
            return d
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= ni < R and 0 <= nj < C and (ni, nj) not in seen and height(grid[ni][nj]) <= height(grid[i][j]) + 1:
                q.append((ni, nj, d + 1))
                seen.add((ni, nj))
    return -1


with open("./day_12.txt", 'r') as file:
    lines = file.read().strip().split()

grid = [list(line) for line in lines]
R = len(grid)
C = len(grid[0])

start = None
end = None
for i in range(R):
    for j in range(C):
        char = grid[i][j]
        if char == "S":
            start = i, j
        if char == "E":
            end = i, j

print(bfs(grid, R, C, start, end))
print(multi_source(grid, R, C))