import sys

N = int(sys.stdin.readline())
pair = int(sys.stdin.readline())


graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(pair):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(start):
    global result

    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            result += 1
            dfs(i)

result = 0
visited[1] = True
dfs(1)
print(result)