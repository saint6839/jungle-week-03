import sys

sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

isConnected = [[False for _ in range(N+1)] for _ in range(N+1)]
isVisits = [False for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    isConnected[u][v] = True
    isConnected[v][u] = True

def dfs(start):
    isVisits[start] = True

    for i in range(1, N+1):
        if not isVisits[i] and (isConnected[i][start] or isConnected[start][i]):
            dfs(i)

result = 0
for i in range(1, N+1):
    if not isVisits[i]:
        result += 1
        dfs(i)

print(result)
