with open('2021/day_9/day_9.txt') as file:
    data = file.read()

A = [n for n in data.split('\n')]
B = []
for i in range(len(A)):
	lst = []
	for j in range(len(A[i])):
		lst.append(int(A[i][j]))
	B.append(lst)


def f(arr):
	lst = []
	R = len(arr)
	C = len(arr[0])
	for i in range(R):
		for j in range(C):
			flag = True
			for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
				if 0 <= ni < R and 0 <= nj < C:
					if arr[ni][nj] <= arr[i][j]:
						flag = False

			if flag:
				# lst.append(arr[i][j] + 1)
				lst.append((i, j))
	return lst

print(f(B))



def f2(arr):
	R, C = len(arr), len(arr[0])
	low_points = f(arr)
	
	def bfs(s, e):
		q = []
		seen = set()
		seen.add((s, e))
		q.append((s, e, 1))
		sz = 1

		while q:
			i, j, d = q.pop(0)
			for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
				if 0 <= ni < R and 0 <= nj < C and (ni, nj) not in seen and arr[i][j] < arr[ni][nj] and arr[ni][nj] != 9:
					seen.add((ni, nj))
					sz += 1
					q.append((ni, nj, d + 1))
		return sz
	
	lst = []
	for i in range(len(low_points)):
		r, c = low_points[i]
		ans = bfs(r, c)
		lst.append(ans)

	lst.sort()
	return lst[-1] * lst[-2] * lst[-3]
print(f2(B))


