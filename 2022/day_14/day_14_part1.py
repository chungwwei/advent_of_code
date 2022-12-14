def flow(i, j, grid):
	if grid[i + 1][j] != '.' and grid[i + 1][j - 1] != '.' and grid[i + 1][j + 1] != '.':
		return (i, j)
	if grid[i + 1][j] == '.':
		return flow(i + 1, j, grid)
	elif grid[i + 1][j - 1] == '.':
		return flow(i + 1, j - 1, grid)
	elif grid[i + 1][j + 1] == '.':
		return flow(i + 1, j + 1, grid)
	

def f(grid):
	res = 0
	for _ in range(1000000):
		try:
			pos = flow(0, 500, grid)	
			x, y = pos
			grid[x][y] = 'O'
			res += 1
		except:
			return res
	# for row in grid:
	# 	print(row[480: 504])
		# print(row)

def flow(i, j, grid):
	if grid[i + 1][j] != '.' and grid[i + 1][j - 1] != '.' and grid[i + 1][j + 1] != '.':
		return (i, j)
	if grid[i + 1][j] == '.':
		return flow(i + 1, j, grid)
	elif grid[i + 1][j - 1] == '.':
		return flow(i + 1, j - 1, grid)
	elif grid[i + 1][j + 1] == '.':
		return flow(i + 1, j + 1, grid)


with open('day_14.txt', 'r') as file:
    data = file.read().split('\n')

floor = 0
paths = []
for line in data:
	pts = line.split('->')
	points = []
	for pt in pts:
		a = pt.split(',')
		y, x = int(a[0]), int(a[1])
		points.append((x, y))
		floor = max(y, floor)
	paths.append(points)

grid = [['.'] * 1000  for _ in range(1000)]
for path in paths:
	for i in range(1, len(path)):
		a, b = path[i - 1]
		c, d = path[i]
		if a == c:
			mn = min(b, d)
			mx = max(b, d)
			for k in range(mn, mx + 1):
				grid[a][k] = '#'
		if b == d:
			mn = min(a, c)
			mx = max(a, c)
			for k in range(mn, mx + 1):
				grid[k][b] = '#'

print(f(grid))

