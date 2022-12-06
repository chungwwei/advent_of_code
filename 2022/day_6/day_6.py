from collections import defaultdict
def f(signals):
	return f2(signals, 4)
			

def f2(signals, k_distinct):
	cnt = defaultdict(int)
	index = -1
	for i in range(len(signals)):
		if i >= k_distinct:
			cnt[signals[i - k_distinct]] -= 1
			if cnt[signals[i - k_distinct]] == 0:
				del cnt[signals[i - k_distinct]]
		cnt[signals[i]] += 1
		if len(cnt) == k_distinct:
			# print(cnt)
			return i + 1
	return index	

with open('./day_6.txt') as file:
	data = file.read()

print(f(data))
print(f2(data, 14))


