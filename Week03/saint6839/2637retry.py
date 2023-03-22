import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]
in_degree = [0 for _ in range(N+1)]
base_items = []

for _ in range(M):
    X, Y, K = map(int, sys.stdin.readline().split())
    graph[Y].append([X, K])
    in_degree[X] += 1

queue = deque()
for i in range(1, N+1):
    if in_degree[i] == 0:
        queue.append(i)
        base_items.append(i)

results = [[0 for _ in range(N+1)] for _ in range(N+1)]

while queue:
    popped = queue.popleft()
    for x, k in graph[popped]:
        if popped in base_items:
            results[x][popped] += k
        else:
            for i in range(1, N+1):
                results[x][i] += results[popped][i] * k
        in_degree[x] -= 1
        if in_degree[x] == 0:
            queue.append(x)

for result in enumerate(results[N]):
    if result[1] > 0:
        print(*result)



