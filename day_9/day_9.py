with open('day_9/day_9.txt') as file:
    data = file.read()

A = [int(n) for n in data.split('\n')]
n = len(A)

def two_sum(nums, k):
    nums.sort()
    i, j = 0, len(nums) - 1
    while i < j:
        if nums[i] + nums[j] < k:
            i += 1
        elif nums[i] + nums[j] > k:
            j -= 1
        else:
            return True
    return False

def part_one(A):
    for i in range(25, len(A)):
        if not two_sum(A[i - 25: i], A[i]):
            return A[i]
    return -1

invalid_num = part_one(A)
print(invalid_num)
def part_two(A):
    P = [0] * (len(A) + 1)
    for i in range(1, len(P)):
        P[i] = P[i - 1] + A[i - 1]
    
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            if P[j] - P[i] == invalid_num:
                a, b = i, j
                lst = A[i: j]
                mn, mx = min(lst), max(lst)
                return mn + mx
    return 0

print(part_two(A))


