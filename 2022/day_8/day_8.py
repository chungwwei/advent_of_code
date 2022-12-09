from collections import defaultdict
def f(matrix):
	R, C = len(matrix), len(matrix[0])
	seen = set()
	
	# edges		
	for j in range(C):
		seen.add((0, j))
		seen.add((R - 1, j))
	
	for i in range(R):
		seen.add((i, 0))
		seen.add((i, C - 1))

	for i in range(R):
		lst = matrix[i]
		n = len(lst)
		mx = lst[0]
		# left to right
		for j in range(1, n - 1):
			if lst[j] > mx:
				seen.add((i, j))
			mx = max(lst[j], mx)
		
		mx = lst[-1]
		for j in range(n - 2, 0, -1):
			if lst[j] > mx:
				seen.add((i, j))
			mx = max(lst[j], mx)
	
	# transpose
	matrix = list(zip(*matrix))
	R, C = len(matrix), len(matrix[0])
	for i in range(R):
		lst = matrix[i]
		n = len(lst)
		mx = lst[0]
		# left to right
		for j in range(1, n - 1):
			if lst[j] > mx:
				seen.add((j, i))
			mx = max(lst[j], mx)
		
		mx = lst[-1]
		for j in range(n - 2, 0, -1):
			if lst[j] > mx:
				seen.add((j, i))
			mx = max(lst[j], mx)
		return len(seen)


def f2(matrix):
	R, C = len(matrix), len(matrix[0])
	res = 0
	for i in range(R):
		for j in range(C):
			height = matrix[i][j]
			score = 1
			for di, dj in [(1, 0), (-1 ,0), (0, 1), (0, -1)]:
				dist = 0
				ni, nj = i + di, j + dj
				while 0 <= ni < R and 0 <= nj < C and matrix[ni][nj] < height:
					dist += 1
					ni += di
					nj += dj
					if 0 <= ni < R and 0 <= nj < C and matrix[ni][nj] >= height:
						dist += 1
				score *= dist
			res = max(res, score)
	return res
				

with open('./day_8.txt', "r") as file:
	data = file.read().split('\n')

data = list(map(list, data))
data = [list(map(int, lst)) for lst in data]
# print(f(data))
# print(f2(data))