from re import U
from typing import Match


with open('2021/day_2/day_2.txt') as file:
    data = file.read()

A = [line for line in data.split('\n')]
A = [line.split() for line in A]

def f(arr):
	n = len(arr)
	depth = 0
	horizontal = 0

	for instruction in arr:
		command, unit = instruction
		unit = int(unit)

		if command == "forward":
			horizontal += unit
		elif command == "down":
			depth += unit
		elif command == "up":
			depth -= unit

	return horizontal * depth


def f2(arr):
	n = len(arr)
	depth = horizontal = aim = 0
	for instruction in arr:
		command, unit = instruction
		unit = int(unit)

		if command == "forward":
			horizontal += unit
			depth += aim * unit
		elif command == "down":
			aim += unit
		elif command == "up":
			aim -= unit

	return horizontal * depth

print(f2(A))

