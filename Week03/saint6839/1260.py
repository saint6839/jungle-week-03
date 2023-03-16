import sys
from collections import deque

sys.setrecursionlimit(10**6)

N, M, V = map(int, sys.stdin.readline().split())

isConnected = [[False for _ in range(N+1)] for _ in range(N+1)]
isVisits = [False for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    isConnected[start][end] = True
    isConnected[end][start] = True

results = []
def dfs(start):
    isVisits[start] = True
    results.append(start)

    for i in range(1, N+1):
        if not isVisits[i] and (isConnected[start][i] or isConnected[i][start]):
            dfs(i)

queue = deque()
def bfs(start):
    isVisits[start] = True
    queue.append(start)

    while queue:
        popped = queue.popleft()
        results.append(popped)
        for i in range(1, N+1):
            if not isVisits[i] and (isConnected[popped][i] or isConnected[i][popped]):
                isVisits[i] = True
                queue.append(i)

dfs(V)
print(*results)
results = []
isVisits = [False for _ in range(N+1)]
bfs(V)
print(*results)


