def f(A):
    res = 0 
    for i, line in enumerate(A):
        a = b = 0
        seen = False
        for j, v in enumerate(line):
            if not v.isdigit():
                continue
            if not seen:
                a = int(v)
                seen = True
            b = int(v)
        print(f"{a}{b}")
        res += int(f"{a}{b}")

    return res

def f2(A):
    D = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            "1", "2", "3", "4", "5", "6", "7", "8", "9"
        ]
    
    mp = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4, 
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    res = 0
    for _, line in enumerate(A):
        first_letter_digit = None
        last_letter_digit = None
        mn = len(line) + 1
        mx = -1
        for d in D:
            if line.find(d) != -1 and line.find(d) <= mn:
                first_letter_digit = d
                mn = min(mn, line.find(d))
            if line.rfind(d) != -1 and line.rfind(d) >= mx:
                last_letter_digit = d
                mx = max(mx, line.rfind(d))

        if not first_letter_digit.isdigit():
            first_letter_digit = int(mp[first_letter_digit])
        if not last_letter_digit.isdigit():
            last_letter_digit = int(mp[last_letter_digit])
        print(f"{first_letter_digit}{last_letter_digit}")
        res += int(f"{first_letter_digit}{last_letter_digit}")
    return res

with open('./part_2.txt') as file:
    data = file.read()

A = data.split('\n')
print(A)
# print(f(A))
print(f2(A))