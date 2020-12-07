with open('day_7/day_7.txt') as file:
    data = file.read()

A = [n for n in data.split('\n')]
n = len(A)

seen = set()
import collections
edges = collections.defaultdict(set)

def dfs(color):
    print(color)
    if color in seen:
        return
    seen.add(color)
    for child in edges[color]:
        dfs(child)

def part_one():

    for rule in A:
        rule = rule.replace('bags', '').replace('bag','').replace(',', '').replace('.', '').replace(' ','')
        parts = rule.split('contain')
        
        wrap_color = parts[0]

        child_colors = parts[1]
        for i in range(1, 10, 1):
            child_colors = child_colors.replace(str(i), '$')
        child_colors = child_colors[1:]
        child_colors = child_colors.split('$')

        for child in child_colors:
            edges[child].add(wrap_color)
    
    # edges: edge child -> parent(wrap color)    
    dfs('shinygold')



# part_one()
# print(len(seen) - 1)

def part_two():
    edges = collections.defaultdict(set)
    for rule in A:
        rule = rule.replace('bags', '').replace('bag','').replace('.', '').replace(' ','')
        parts = rule.split('contain')
        
        wrap_color = parts[0]

        child_colors = parts[1]
        if child_colors == 'noother':
            continue
        child_colors = child_colors.split(',')
        for color in child_colors:
            edges[wrap_color].add((int(color[0]), color[1:]))


    res = 0
    bfs = [(1, 'shinygold')]
    while len(bfs) > 0:
        amt, color = bfs.pop(0)
        res += amt

        if color in edges:
            children = edges[color]
            for n, child in children:
                bfs.append((n * amt, child))
    print(res - 1)



part_two()