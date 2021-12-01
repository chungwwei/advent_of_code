def f(A):
	n = len(A)
	res = 0
	for i in range(1, n):
		if A[i] - A[i - 1] > 0:
			res += 1
	return res

with open('2021/day_1.txt') as file:
    data = file.read()

A = [int(n) for n in data.split('\n')]
# print(f(A))


def f2(A):
	size = 3
	total = 0
	i = 0
	prev = 0
	res = 0
	for j in range(len(A)):
		total += A[j]
		if j - i + 1 > size:
			total -= A[i]
			i += 1 
		
		if j - i + 1 == size:
			if j == 2:
				prev = total
				continue
			if total > prev:
				res += 1
			prev = total
			
	return res

print(f2(A))
		