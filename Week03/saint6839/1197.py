import sys

V, E = map(int, sys.stdin.readline().split())

parent = [0 for _ in range(V+1)]

for i in range(1, V+1):
    parent[i] = i

edges = []
for _ in range(E):
    edges.append(tuple(map(int, sys.stdin.readline().split())))


edges.sort(key= lambda x: x[2])

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(start, end):
    start = find(start)
    end = find(end)
    if start < end:
        parent[end] = start
    else:
        parent[start] = end

result = 0
for i in range(E):
    start, end, cost = edges[i]
    if find(start) != find(end):
        union(start, end)
        result += cost

print(result)
