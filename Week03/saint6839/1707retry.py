import sys
from collections import deque

K = int(sys.stdin.readline())


def bfs(start):
    queue = deque()
    visited[start] = 1
    queue.append(start)

    while queue:
        popped = queue.popleft()
        for i in graph[popped]:
            if not visited[i] and visited[popped] == 1:
                visited[i] = 2
                queue.append(i)
            elif not visited[i] and visited[popped] == 2:
                visited[i] = 1
                queue.append(i)
            elif visited[i] == 1 and visited[popped] == 1:
                return False
            elif visited[i] == 2 and visited[popped] == 2:
                return False

    return True

for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V+1):
        if not visited[i]:
            flag = bfs(i)
            if not flag:
                break

    if flag:
        print("YES")
    else:
        print("NO")

