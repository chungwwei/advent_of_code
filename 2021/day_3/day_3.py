from re import U
from typing import Literal, Match


with open('2021/day_3/day_3.txt') as file:
    data = file.read()

A = [line for line in data.split('\n')]


def binary_int_to_decimal(binary):
    n = 0
    for d in binary:
        n = n * 2 + int(d)

    return n

def f(arr):
	if not arr:
		return 0
	n = len(arr[0])
	one_count = [0] * n
	zero_count = [0] * n
	most_common = [0] * n
	least_common = [0] * n

	for lst in arr:
		for i in range(n):
			if lst[i] == '1':
				one_count[i] += 1
			else:
				zero_count[i] += 1
	for i in range(n):
		most_common[i] = 1 if one_count[i] > zero_count[i] else 0
		least_common[i] = 1 if one_count[i] < zero_count[i] else 0
	
	
	return binary_int_to_decimal(most_common) * binary_int_to_decimal(least_common)


def bit_cnt(input: list, pos: int) -> int:
    return len(list(filter(lambda x: x[pos] == '1', input)))


def filter_cand(fn, candidates) -> int:
    n = 0
    while len(candidates) > 1:
        if fn(bit_cnt(candidates, n) * 2, len(candidates)):
            candidates = list(filter(lambda x: x[n] == '1', candidates))
        else:
            candidates = list(filter(lambda x: x[n] == '0', candidates))
        n += 1

    return int(candidates[0], 2)


def f2(arr):
    a = filter_cand(lambda a, b: a >= b, arr)
    b = filter_cand(lambda a, b: a < b, arr)

    return a * b

print(f2(A))