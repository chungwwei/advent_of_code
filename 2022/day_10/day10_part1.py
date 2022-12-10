from collections import deque
def f(data):
	cycles, v = 1, 1
	total = 0
	q = deque()
	for op in data:
		if len(op) > 1:
			operator = op[0]
			val = int(op[1])
			q.append([val, cycles + 2])
			cycles += 2
		else:
			cycles += 1


	for cycle in range(1, 1000):
		if cycle in [20, 60, 100, 140, 180, 220]:
			total += cycle * v
		while q and q[0][-1] == cycle + 1:
			element = q.popleft()
			v += element[0]

	return total

with open('./day_10.txt') as file:
	data = file.read().split('\n')

data = [item.split(' ') for item in data]
print(f(data))