import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)

visited = [False for _ in range(N+1)]

results = []
def bfs(start):
    queue = deque()
    queue.append([start, 0])
    visited[start] = True

    while queue:
        ps, pcost = queue.popleft()
        if pcost == K:
            results.append(ps)

        for i in graph[ps]:
            if not visited[i]:
                visited[i] = True
                queue.append([i, pcost + 1])

bfs(X)
if not results:
    print(-1)
else:
    results.sort()
    for result in results:
        print(result)

