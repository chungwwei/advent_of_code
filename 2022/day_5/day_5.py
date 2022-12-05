from collections import deque
def f(rows, commands, N):
	stacks = [[] for _ in range(N)]
	for row in rows:
		for i, c in enumerate(row):
			if c != '':
				stacks[i].append(c)

	for q, src, des in commands:
		while q > 0:
			if len(stacks[src]) == 0:
				break
			stacks[des].append(stacks[src].pop())
			q -= 1

	return "".join([stack[-1] for stack in stacks])

def f2(rows, commands, N):
	stacks = [[] for _ in range(N)]
	for row in rows:
		for i, c in enumerate(row):
			if c != '':
				stacks[i].append(c)

	for q, src, des in commands:
		d = deque([])
		while q > 0:
			if len(stacks[src]) == 0:
				break
			d.append(stacks[src].pop())
			q -= 1
		while len(d) > 0:
			stacks[des].append(d.pop())

	return "".join([stack[-1] for stack in stacks])

with open('./day_5.txt') as file:
	data = file.read().split('\n')

index = data.index('')
arr = data[:index]
commands = data[index + 1:]
rows = list(map(lambda x: x.replace('[', '').replace(']', '').replace('    ', ' ').split(' '), arr[:-1]))[::-1]
indices = list(map(int, arr[-1].strip().split('   ')))
commands = list(map(lambda x: x.split(' '), commands))
commands = list(map(lambda x: (int(x[1]), int(x[3]) - 1, int(x[5]) - 1), commands))
print(f(rows, commands, len(indices)))
print(f2(rows, commands, len(indices)))



