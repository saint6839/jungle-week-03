import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(N+1):
    graph[i].sort()

results = []
visited = [False for _ in range(N+1)]


def dfs(start, depth):
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            print(i, end=' ')
            dfs(i, depth + 1)


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    results.append(start)

    while queue:
        popped = queue.popleft()

        for i in graph[popped]:
            if not visited[i]:
                visited[i] = True
                results.append(i)
                queue.append(i)


results.append(V)
visited[V] = True
print(V, end=' ')
dfs(V, 1)
print()

results = []
visited = [False for _ in range(N+1)]
bfs(V)

print(*results)