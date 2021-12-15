from collections import defaultdict
import heapq

with open('2021/day_15/day_15.txt') as file:
    data = file.read()

A = [n for n in data.split('\n')]
B = []
for lst in A:
	temp = []
	for n in lst:
		temp.append(int(n))
	B.append(temp)


def shortest_path(arr):
	if not arr:
		return 0
	R, C = len(arr), len(arr[0])
	q = [(0, 0, 0)]
	dist = defaultdict(lambda: float('inf'))
	dist[(0, 0)] = 0
	heapq.heapify(q)

	while q:
		d, i, j = heapq.heappop(q)
		for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
			if 0 <= ni < R and 0 <= nj < C:
				edge_weight = arr[ni][nj] + d
				if edge_weight < dist[(ni, nj)]:
					dist[(ni, nj)] = edge_weight
					q.append((edge_weight, ni, nj))

	return dist[(R - 1, C - 1)]

# print(shortest_path(B))