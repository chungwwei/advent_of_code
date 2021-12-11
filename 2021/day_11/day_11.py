with open('2021/day_11/day_11.txt') as file:
    data = file.read()

A = [n for n in data.split('\n')]
B = []
for i in range(len(A)):
	lst = []
	for j in range(len(A[i])):
		lst.append(int(A[i][j]))
	B.append(lst)

def f(A):
	def bfs():
		flashes = set()
		q = []
		res = 0
		for i in range(10):
			for j in range(10):
				A[i][j] += 1
				if A[i][j] > 9:
					A[i][j] = 0
					q.append((i, j))
					flashes.add((i, j))
					res += 1
		while q:
			i, j = q.pop()
			for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i + 1, j + 1), (i + 1, j - 1), (i - 1, j - 1), (i - 1, j + 1)]:
				if 0 <= ni < 10 and 0 <= nj < 10 and (ni, nj) not in flashes:
					A[ni][nj] += 1
					if A[ni][nj] > 9:
						q.append((ni, nj))
						A[ni][nj] = 0
						flashes.add((ni, nj))
						res += 1
		return res
	
	days = 0
	total = 0
	while days < 100:
		total += bfs()
		days += 1
	return total

# print(f(B))


def f2(A):
	def bfs():
		flashes = set()
		q = []
		res = 0
		for i in range(10):
			for j in range(10):
				A[i][j] += 1
				if A[i][j] > 9:
					A[i][j] = 0
					q.append((i, j))
					flashes.add((i, j))
					res += 1
		while q:
			i, j = q.pop()
			for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i + 1, j + 1), (i + 1, j - 1), (i - 1, j - 1), (i - 1, j + 1)]:
				if 0 <= ni < 10 and 0 <= nj < 10 and (ni, nj) not in flashes:
					A[ni][nj] += 1
					if A[ni][nj] > 9:
						q.append((ni, nj))
						A[ni][nj] = 0
						flashes.add((ni, nj))
						res += 1
	
	days = 1
	while True:
		bfs()
		if all(x == 0 for line in A for x in line):
			return days
		days += 1

print(f2(B))

	

				
		