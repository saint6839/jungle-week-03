import sys
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().split())


graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(N+1)]

def dfs(start):

    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

result = 0
for i in range(1, N+1):
    if not visited[i]:
        result += 1
        visited[i] = True
        dfs(i)

print(result)

