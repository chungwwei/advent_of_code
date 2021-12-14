from collections import Counter

with open('2021/day_14/day_14.txt') as file:
    data = file.read()

A = [n for n in data.split('\n')]
template = A[0]
r = A[2:]
rules = {}
for rule in r:
	pair, insert = rule.split("->")
	pair = pair.strip()
	insert = insert.strip()
	rules[pair] = insert


# print(template)
# print(rules)

def transform(t):
	new_template = []
	for i in range(len(t) - 1):
		pair = t[i] + t[i + 1]
		if pair in rules:
			new_template.append(t[i])
			new_template.append(rules[pair])
		else:
			new_template.append(t[i])
	new_template.append(t[-1])

	return "".join(new_template)


def f(template):
	steps = 1
	while steps <= 40:
		template = transform(template)
		# print(template)
		steps += 1
	
	cnt = Counter(template)
	lst = cnt.values()
	mx = max(lst)
	mn = min(lst)
	return mx - mn

print(f(template=template))
