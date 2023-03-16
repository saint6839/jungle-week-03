import sys
from collections import deque

N = int(sys.stdin.readline())
pair = int(sys.stdin.readline())

isConnected = [[False for _ in range(N+1)] for _ in range(N+1)]
isVisits = [False for _ in range(N+1)]

for _ in range(pair):
    a, b = map(int, sys.stdin.readline().split())
    isConnected[a][b] = True
    isConnected[b][a] = True


queue = deque()
result = 0
def bfs(start):
    global result

    isVisits[start] = True
    queue.append(start)

    while queue:
        popped = queue.popleft()
        for i in range(1, N+1):
            if not isVisits[i] and (isConnected[popped][i] or isConnected[i][popped]):
                isVisits[i] = True
                result += 1
                queue.append(i)

bfs(1)
print(result)