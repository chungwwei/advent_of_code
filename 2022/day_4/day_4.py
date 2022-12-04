def contain(A, B):
	a, b = A
	c, d = B

	'''
		c....a....b....d
	'''
	if c <= a and b <= d:
		return True

def f(pairs):
	res = 0
	for pair in pairs:
		first = pair[0]
		second = pair[1]
		if contain(first, second):
			res += 1
		elif contain(second, first):
			res += 1
	return res

def f2(pairs):
	res = 0
	for pair in pairs:
		pair.sort(key=lambda x: x[0])
		first = pair[0]
		second = pair[1]
		if second[0] <= first[1]:
			res += 1

	return res


with open('./day_4.txt') as file:
    data = file.read()

A = data.split('\n')
pairs = []
for intervals in A:
    p = intervals.split(',')
    a, b = p[0].split('-'), p[1].split('-')
    pairs.append([(int(a[0]), int(a[1])), (int(b[0]), int(b[1]))])

# print(pairs)
print(f(pairs))
print(f2(pairs))