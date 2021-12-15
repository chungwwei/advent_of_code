import heapq
from collections import defaultdict

with open("2021/day_15/day_15.txt") as file:
    raw_data = file.read().strip()
map = [[int(i) for i in line] for line in raw_data.split("\n")]


R = len(map)
C = len(map[0])

rows = R * 5
cols = C * 5


def get(r, c):
    x = (map[r % R][c % C] +
         (r // R) + (c // C))
    return (x - 1) % 9 + 1


dist = defaultdict(int)

q = [(0, 0, 0)]
heapq.heapify(q)
visited = set()

while q:
    c, row, col = heapq.heappop(q)

    if (row, col) in visited:
        continue
    visited.add((row, col))

    dist[(row, col)] = c

    if row == rows - 1 and col == cols - 1:
        break

    for rr, cc in [(row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1)]:
        if not (0 <= rr < rows and 0 <= cc < cols):
            continue
        heapq.heappush(q, (c + get(rr, cc), rr, cc))


print(dist[(rows - 1, cols - 1)])