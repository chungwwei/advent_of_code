from collections import deque

# def bfs(start, end):
# 	seen = set()
# 	print((start, end))
# 	q = deque()
# 	q.append((start[0], start[1], 0))
# 	seen.add(start)
# 	while q:
# 		i, j, d = q.popleft()
# 		if (i, j) == end:
# 			print(f"end with distance: {d}")
# 			# while q[0][-1] == d:
# 			# 	i, j, d = q.popleft()
# 			# 	seen.add((i, j))
# 			break
			
# 		for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
# 			if (ni, nj) not in seen:
# 				q.append((ni, nj, d + 1))
# 				seen.add((ni, nj))
# 	return seen

# part_1
def f(pairs, beacons):
	res = 0
	def within(x, y):
		for pair in pairs:
			sx, sy = pair[0]
			d = pair[-1]
			diff = abs(x - sx) + abs(y - sy)
			if diff <= d:
				return False
		return True

	# for x in range(-10, 100):
	for x in range(-int(1e7), int(1e7)):
		y = int(2e6)
		if not within(x, y) and (x, y) not in beacons:
			res += 1
	return res
	# 583939 too low


def f2(A):
    pass

with open('day_15.txt', 'r') as file:
    lines = file.read().split('\n')
	
# sensor-beacon pair
pairs = []
beacons = set()
for line in lines:
	tokens = line.split(' ')
	sensor_x = tokens[2].replace(',', '')
	sensor_y = tokens[3].replace(':', '')
	beacon_x = tokens[-2].replace(',', '')
	beacon_y = tokens[-1]

	sensor_x = int(sensor_x.split('=')[-1])
	sensor_y = int(sensor_y.split('=')[-1])
	beacon_x = int(beacon_x.split('=')[-1])
	beacon_y = int(beacon_y.split('=')[-1])

	d = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

	beacons.add((beacon_x, beacon_y))
	pairs.append(((sensor_x, sensor_y), (beacon_x, beacon_y), d))

# print(pairs)
print(f(pairs, beacons))