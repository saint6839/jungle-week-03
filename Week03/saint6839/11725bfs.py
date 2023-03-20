import sys
from collections import deque

N = int(sys.stdin.readline())
connections = [[] for _ in range(N+1)]
isVisits = [False for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    connections[a].append(b)
    connections[b].append(a)


queue = deque()
results = dict()
def bfs(start):
    isVisits[start] = True
    queue.append(start)

    while queue:
        popped = queue.popleft()
        for i in connections[popped]:
            if not isVisits[i]:
                isVisits[i] = True
                queue.append(i)
                results[i] = popped
bfs(1)
for i in range(2, N+1):
    print(results[i])

