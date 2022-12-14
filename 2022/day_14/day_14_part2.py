def flow(floor):
	global seen
	i, j = 500, 0
	if (i, j) in seen:
		return (i, j)
	
	while j <= floor:
		if (i, j + 1) not in seen:
			j += 1
			continue
		if (i - 1, j + 1) not in seen:
			i -= 1
			j += 1
			continue
		if (i + 1, j + 1) not in seen:
			i += 1
			j += 1
			continue
		else:
			break
	return (i, j)

	
def f(floor):
	res = 0
	while 1:
		i, j = flow(floor)
		seen.add((i, j))
		res += 1
		if (i, j) == (500, 0):
			break
	return res

with open('day_14.txt', 'r') as file:
    data = file.read().split('\n')

paths = []
floor = 0
seen = set()
for line in data:
	pts = line.split('->')
	points = []
	for pt in pts:
		x, y = map(int, pt.split(","))
		points.append((x, y))
		floor = max(y, floor)
	paths.append(points)

for path in paths:
	for i in range(1, len(path)):
		a, b = path[i - 1]
		c, d = path[i]
		if a == c:
			mn = min(b, d)
			mx = max(b, d)
			for k in range(mn, mx + 1):
				seen.add((a, k))
		if b == d:
			mn = min(a, c)
			mx = max(a, c)
			for k in range(mn, mx + 1):
				seen.add((k, b))

print(f(floor))

