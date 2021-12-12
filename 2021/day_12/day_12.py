from collections import defaultdict

with open('2021/day_12/day_12.txt') as file:
    data = file.read()

A = [n for n in data.split('\n')]
adj = defaultdict(list)
for line in A:
    u, v = line.split('-')
    adj[u].append(v)
    adj[v].append(u)

res = 0
visited = set()

def is_small(root):
    return root.islower()

def dfs(root):
    global res
    if root == 'end':
        res += 1
        return 
    if is_small(root) and root in visited:
        return
    
    if is_small(root):
        visited.add(root)
    
    for nei in adj[root]:
        if nei == 'start':
            continue
        dfs(nei)
    
    if is_small(root):
        visited.remove(root)
    


# dfs('start')
# print(res)
res = 0
visited = defaultdict(int)
def dfs2(root):

    global res
    if root == 'end':
        res += 1
        return 

    if is_small(root):
        visited[root] += 1
    
        cnt = 0
        for small in visited:
            cnt += visited[small] > 1

            if visited[small] > 2:
                visited[root] -= 1
                return
        
        if cnt > 1:
            visited[root] -= 1
            return
    
    for nei in adj[root]:
        if nei == 'start':
            continue
        dfs2(nei)
    
    if is_small(root):
        visited[root] -= 1

dfs2('start')
print(res)


