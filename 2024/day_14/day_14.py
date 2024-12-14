def print_pos(pos):
    X, Y = 101, 103
    m = [[0 for _ in range(X)] for _ in range(Y)]

    for x, y in pos:
        m[y][x] += 1

    for i in range(Y):
        temp = []
        for j in range(X):
            if m[i][j] > 0:
                temp.append('#')
            else:
                temp.append(' ')
        print("".join(temp))



def f(robots):
    X, Y = 101, 103
    hx, hy = X // 2, Y // 2
    res = []
    q1 = q2 = q3 = q4 = 0
    for robot in robots:
        pos, velocity = robot
        x, y = pos
        dx, dy = velocity
        x = (x + 100 * dx) % X
        y = (y + 100 * dy) % Y
        # for _ in range(100):
        #     x = (x + dx) % X
        #     y = (y + dy) % Y

        if x == X // 2 or y == Y // 2: continue
        res.append((x, y))
        quad1 = x < hx and y < hy
        quad2 = x > hx and y < hy
        quad3 = x < hx and y > hy
        quad4 = x > hx and y > hy
        if quad1: q1 += 1
        if quad2: q2 += 1
        if quad3: q3 += 1
        if quad4: q4 += 1

    return q1 * q2 * q3 * q4

def f2(robots):
    X, Y = 101, 103
    N = len(robots)
    res = []
    out = 0
    for t in range(10**5):
        seen = set()
        res = []
        for robot in robots:
            pos, velocity = robot
            x, y = pos
            dx, dy = velocity
            x = (x + t * dx) % X
            y = (y + t * dy) % Y
            seen.add((x, y))
            res.append((x, y))
        if len(seen) == N:
            out = t
            break
    print_pos(res)
    return out


with open('./input.txt') as file:
    data = file.read().strip()

lines = data.split("\n")
robots = []
for line in lines:
    coords, velocities =line.split(" ")
    x = coords.split(',')[0].split('=')[-1]
    y = coords.split(',')[-1]
    x, y = int(x), int(y)

    dx = velocities.split(',')[0].split('=')[-1]
    dy = velocities.split(',')[-1]
    dx, dy = int(dx), int(dy)

    robots.append(((x,y), (dx, dy)))

print(f(robots))
print(f2(robots))
