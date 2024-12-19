def f(towels, designs):
    cache = {}
    def dfs(design):
        if design in cache: return cache[design]
        if design == '': return True

        res = False
        for towel in towels:
            if design.startswith(towel):
                res = res or dfs(design[len(towel):])
        cache[design] = res
        return res

    cnt = 0
    for design in designs:
        if dfs(design):
            cnt += 1

    return cnt

def f2(towels, designs):
    cache = {}
    def dfs(design):
        if design in cache: return cache[design]
        if design == '': return 1

        res = 0
        for towel in towels:
            if design.startswith(towel):
                res += dfs(design[len(towel):])
        cache[design] = res
        return res

    cnt = 0
    for design in designs:
        cnt += dfs(design)

    return cnt


with open('./input.txt') as file:
    data = file.read().strip()

lines = data.split("\n")
designs = []
towels = lines[0].split(',')
towels = [t.strip().strip() for t in towels]
for line in lines[2:]:
    designs.append(line)

print(f(towels, designs))
print(f2(towels, designs))
