import math
class Monkey():
	def __init__(self, id, items, op, divisor, to_true, to_false):
		self.id = id
		self.items = items
		self.op = op
		self.divisor = divisor
		self.to_false = to_false 
		self.to_true = to_true

	def is_divisible(self, n):
		if self.divisor == 0:
			return False
		return n % self.divisor == 0

	def do_op(self, old):
		operator, val = self.op
		if operator == '*':
			if val == 'old':
				return old ** 2
			else:
				return old * int(val)
		if operator == '+':
			if val == 'old':
				return old + old
			else:
				return old + int(val)

	def process(self, item):
		new_val = self.do_op(item)
		# turn on for part_1
		# new_val //= 3 
		return (self.to_true, new_val) if self.is_divisible(new_val) else (self.to_false, new_val)


	def __str__(self):
		return f'items: {self.items}, true: {self.to_true}, false: {self.to_false}'

def f(M):
	cnt = [0] * len(M)
	for _ in range(20):
		for i, m in enumerate(M):
			if len(m.items) <= 0:
				continue
			cnt[i] += len(m.items)
			for _ in range(len(m.items)):
				item = m.items.pop(0)
				throw, level = m.process(item)
				M[throw].items.append(level)
				# print((item, throw, level))
		# s= "\n".join(map(str, M))
		# print(s)
	cnt.sort()
	return cnt[-1] * cnt[-2]

def f2(M, LCM):
	cnt = [0] * len(M)
	for _ in range(10000):
		for i, m in enumerate(M):
			if len(m.items) <= 0:
				continue
			cnt[i] += len(m.items)
			for _ in range(len(m.items)):
				# reduce the big number
				item = m.items.pop(0) % LCM
				throw, level = m.process(item)
				M[throw].items.append(level)
				# print((item, throw, level))
		# s= "\n".join(map(str, M))
		# print(s)
	cnt.sort()
	return cnt[-1] * cnt[-2]


with open('./day_11.txt') as file:
	data = file.read().split('\n\n')


M = []
LCM = 1
for monkey in data:
	lines = monkey.split('\n')
	id = lines[0].split(' ')[-1].replace(':', '')
	id = int(id)
	items = lines[1].split(':')[-1].split(',')
	items = list(map(int, items))
	lines2 = lines[2].split(' ')
	operator = lines2[-2]
	worry_mult = lines2[-1]
	op = (operator, worry_mult)
	divisor = int(lines[3].split(' ')[-1])
	to_true = int(lines[4].split(' ')[-1])
	to_false = int(lines[5].split(' ')[-1])
	m = Monkey(
		id,
		items,
		op,
		divisor,
		to_true,
		to_false,
	)
	LCM *= divisor
	M.append(m)

# print(f(M))
# print(f2(M, LCM))