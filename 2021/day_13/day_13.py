with open("2021/day_13/day_13.txt") as fin:
    dots = set()
    while True:
        line = fin.readline().strip()
        if line == "":
            break
        dots.add(tuple([int(i) for i in line.split(",")]))

    folds = []
    while True:
        line = fin.readline().strip()
        if line == "":
            break

        fold = line[len("fold along "):]
        if fold[0] == "y":
            folds.append((0, int(fold[2:])))
        else:
            folds.append((int(fold[2:]), 0))


def reflect(point, axis):
    x, y = axis
    px, py = point

    if x != 0:
        return (2*x - px, py)
    return (px, 2*y - py)


for fold in folds:
    new_dots = set()

    for dot in dots:
        if fold[0] != 0:
            # Vertical fold
            if dot[0] > fold[0]:
                new_dots.add(reflect(dot, fold))
            else:
                new_dots.add(dot)

        else:
            # Horizontal fold
            if dot[1] > fold[1]:
                new_dots.add(reflect(dot, fold))
            else:
                new_dots.add(dot)
    print(len(new_dots))
    dots = new_dots


	
for y in range(6):
    for x in range(100):
        if (x, y) in new_dots:
            print("#", end="")
        else:
            print(".", end="")
    print()

print(len(new_dots))