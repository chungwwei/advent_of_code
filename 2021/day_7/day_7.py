with open('2021/day_7/day_7.txt') as file:
    data = file.read()

A = [int(n) for n in data.split(',')]


def f(arr):
	mn = sum(arr)
	cands = set(arr)
	for cand in cands:
		s = sum([abs(cand - n) for n in arr])
		mn=  min(mn, s)
	return mn

	
def f2(arr):
	mn = float('inf')
	cands = set(arr)
	for cand in cands:
		s = sum([abs(cand - n) * (abs(cand - n) + 1) // 2 for n in arr])
		mn = min(s, mn)
	return mn

print(f2(A))