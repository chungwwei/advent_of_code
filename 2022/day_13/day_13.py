from functools import cmp_to_key


def dfs(left, right):
	if type(left) == int and type(right) == int:
		if left < right:
			return -1
		if left > right:
			return 1
		return 0
	
	elif type(left) == list and type(right) == list:
		i = 0
		while i < len(left) and i < len(right):
			c = dfs(left[i], right[i])
			if c == -1:
				return -1
			if c == 1:
				return 1
			i += 1
		
		if i == len(left) and i < len(right):
			return -1
		elif i == len(right) and i < len(left):
			return 1
		else:
			return 0
	elif type(left) == int and type(right) == list:
		return dfs([left], right)
	elif type(left) == list and type(right) == int:
		return dfs(left, [right])


def f(pairs):
	res = 0
	for i, pair in enumerate(pairs):
		first, second = pair
		out = dfs(first, second)
		if out == -1:
			res += i + 1
	return res


def f2(lsts):

	lsts.append([[2]])
	lsts.append([[6]])

	lsts = sorted(lsts, key=cmp_to_key(lambda left, right: dfs(left, right)))
	res = 1
	for i, p in enumerate(lsts):
			if p == [[2]] or p == [[6]]:
					res *= i + 1
	return res


with open("./day_13.txt", 'r') as file:
  data = file.read().split("\n\n")

pairs = []
lsts = []
for two_lines in data:
	lst = two_lines.split('\n')
	first, second = lst[0], lst[1]
	first = eval(first)
	second = eval(second)
	pairs.append((first, second))
	lsts.append(first)
	lsts.append(second)

print(f(pairs))
print(f2(lsts))