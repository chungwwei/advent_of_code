with open('day_3/day_3.txt') as file:
    data = file.read()

A = [[n for n in lst] for lst in data.split('\n')]
def part_one(right, down):
    R, C = len(A), len(A[0])
    res = 0
    i, j = 0, 0
    while i + 1 < R:

        i += down
        j += right 
        if A[i][j % C] == '#':
            res += 1
    return res

def part_two():
    slopes = [[1,1],[3, 1],[5,1],[7,1],[1,2]]
    prod = 1
    for x, y in slopes:
        prod *= part_one(x, y)
    print(prod)

part_two()

 
