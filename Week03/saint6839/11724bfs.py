import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

isConnected = [[False for _ in range(N+1)] for _ in range(N+1)]
isVisits = [False for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    isConnected[u][v] = True
    isConnected[v][u] = True

def bfs(start):
    isVisits[start] = True
    queue.append(start)

    while queue:
        popped = queue.popleft()
        for i in range(1, N+1):
            if not isVisits[i] and (isConnected[i][popped] or isConnected[popped][i]):
                isVisits[i] = True
                queue.append(i)

queue = deque()
result = 0
for i in range(1, N+1):
    if not isVisits[i]:
        result += 1
        bfs(i)

print(result)