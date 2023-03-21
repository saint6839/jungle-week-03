import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()

results = dict()

def dfs(start):
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
            results[i] = start

visited[1] = True
dfs(1)

for i in range(2, N+1):
    print(results[i])

