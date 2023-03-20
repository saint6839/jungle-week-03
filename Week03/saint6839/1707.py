import sys
from collections import deque

sys.setrecursionlimit(10**6)
K = int(sys.stdin.readline())


def bfs(start, color):
    isVisits[start] = color
    queue.append(start)

    while queue:
        popped = queue.popleft()
        for i in graph[popped]:
            if not isVisits[i]:
                queue.append(i)
                isVisits[i] = -1 * isVisits[popped]
            else:
                if isVisits[i] == isVisits[popped]:
                    return False
    return True

for _ in range(K):
    index = 0
    V, E = map(int,sys.stdin.readline().split())
    isVisits = [0 for _ in range(V+1)]

    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int,sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    queue = deque()

    for i in range(1, V+1):
        if not isVisits[i]:
            yes_or_no = bfs(i, 1)
            if not yes_or_no:
                break

    if yes_or_no:
        print('YES')
    else:
        print('NO')
