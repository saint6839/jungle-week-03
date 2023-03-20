import sys

V, E = map(int, sys.stdin.readline().split())

edges = []
for _ in range(E):
    edges.append(list(map(int, sys.stdin.readline().split())))

edges.sort(key= lambda x: x[2])

parent_nodes = [0 for _ in range(V+1)]
for i in range(1, V+1):
    parent_nodes[i] = i

def find(x):
    if parent_nodes[x] != x:
        parent_nodes[x] = find(parent_nodes[x])
    return parent_nodes[x]

def union(start, end):
    start = find(start)
    end = find(end)
    if start < end:
        parent_nodes[end] = start
    else:
        parent_nodes[start] = end

result = 0
for i in range(len(edges)):
    start, end, weight = edges[i]
    if find(start) != find(end):
        union(start, end)
        result += weight

print(result)