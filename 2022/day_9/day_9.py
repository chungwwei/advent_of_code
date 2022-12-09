def is_touching(x1, y1, x2, y2):
	return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1

dirs = {
	'R': (0, 1),
	'L': (0 , -1),
	"U": (1, 0),
	"D": (-1, 0),
}

def f(arr):
	seen = set()
	x, y = 0, 0
	seen.add((x, y))
	H = [x, y]
	T = [x, y]
	hx, hy = H
	tx, ty = T
	for dir, step in arr:
		dx, dy = dirs[dir]
		for _ in range(step):
			hx += dx
			hy += dy
			if not is_touching(hx, hy, tx, ty):
				diff_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
				diff_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)
				tx += diff_x
				ty += diff_y
			seen.add((tx, ty))
	return len(seen)


def move2(knots, dx, dy):
	knots[0][0] += dx
	knots[0][1] += dy

	for i in range(1, 10):
		hx, hy = knots[i - 1]
		tx, ty = knots[i]

		if not is_touching(hx, hy, tx, ty):
			diff_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
			diff_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)
			tx += diff_x
			ty += diff_y
		knots[i] = [tx, ty]


def f2(arr):
	knots = [[0, 0] for _ in range(10)]
	seen = set()
	x, y = 0, 0
	seen.add((x, y))
	H = [x, y]
	T = [x, y]
	hx, hy = H
	tx, ty = T
	for dir, step in arr:
		dx, dy = dirs[dir]
		for _ in range(step):
			move2(knots, dx, dy)
			seen.add(tuple(knots[-1]))


	return len(seen)


with open('./day_9.txt', 'r') as file:
	data = file.read().split('\n')

arr = []
for line in data:
	dir, step = line.split(' ')
	step = int(step)
	arr.append((dir, step))

print(f(arr))
print(f2(arr))


