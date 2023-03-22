import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

visited = [False for _ in range(N+1)]
queue = deque()
results = []
def bfs(start, distance):
    queue.append([start, distance])
    visited[start] = True

    while queue:
        popped = queue.popleft()

        for i in graph[popped[0]]:
            if not visited[i]:
                visited[i] = True
                queue.append([i, popped[1] + 1])

        if popped[1] == K:
            results.append(popped[0])

bfs(X, 0)

results.sort()
if results:
    print(*results, sep='\n')
else:
    print(-1)

