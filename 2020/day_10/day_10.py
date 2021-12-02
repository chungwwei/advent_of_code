with open('day_10/day_10.txt') as file:
    data = file.read()

A = [int(n) for n in data.split('\n')]
n = len(A)

def part_one(A):
    import collections
    cnt = collections.defaultdict(int)
    A.sort()
    A.append(A[-1] + 3)
    last = 0
    for a in A:
        cnt[a - last] += 1
        last = a
    
    print(cnt)
    return cnt[1] * cnt[3]

# print(part_one(A))


###################################
###################################
###################################
A.insert(0, 0)
A.sort()
from functools import lru_cache
@lru_cache(None)
def dp(i):

    if i == len(A) - 1:
        return 1

    total = 0
    j = i + 1
    #print(index, nextIndex)
    while j < len(A) and A[j] - A[i] <= 3:
        total += dp(j)
        j += 1

    return total

ans = dp(0)
print(ans)

