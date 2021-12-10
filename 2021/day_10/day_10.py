from collections import defaultdict


with open('2021/day_10/day_10.txt') as file:
    data = file.read()

A = [n for n in data.split('\n')]


def find_first(arr):
	stk = []
	for i in range(len(arr)):
		if arr[i] == '(' or arr[i] == '[' or arr[i] == '<' or arr[i] == '{':
			stk.append(arr[i])
		else:
			if arr[i] == ')' and stk[-1] == '(':
				stk.pop()
			elif arr[i] == '}' and stk[-1] == '{':
				stk.pop()
			elif arr[i] == '>' and stk[-1] == '<':
				stk.pop()
			elif arr[i] == ']' and stk[-1] == '[':
				stk.pop()
			else:
				return (arr[i], False)
	
	return (stk, True)


def f(arr):
	n = len(arr)
	lst = []
	for i in range(n):
		item, booo = find_first(arr[i])
		if not booo:
			lst.append(item)

	d = {
		')': 3,
		']': 57,
		'}': 1197,
		'>': 25137
	}

	res = 0
	for c in lst:
		res += d[c]
	return res



print(f(A))

def f2(arr):
	n = len(arr)
	scores = []
	for i in range(n):
		item, booo = find_first(arr[i])
		if booo:
			stk = item
		

		lst = []
		while stk:
			lst.append(stk.pop())
		d = {
			'(': 1,
			'[': 2,
			'{': 3,
			'<': 4
		}

		lo = 0
		for c in lst:
			lo *= 5
			lo += d[c]
		if lo != 0:
			scores.append(lo)
	scores.sort()
	return scores[len(scores) // 2]

print(f2(A))

		

	