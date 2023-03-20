import heapq
import sys

V, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append([C, B])
    graph[B].append([C, A])

visited = [False for _ in range(V+1)]

def bfs():
    priority_queue = []
    visited[1] = True
    result = 0
    for i in graph[1]:
        heapq.heappush(priority_queue, i)


    while priority_queue:
        pcost, pnode = heapq.heappop(priority_queue)
        if visited[pnode]:
            continue
        visited[pnode] = True
        result += pcost

        for i in graph[pnode]:
            if not visited[i[1]]:
                heapq.heappush(priority_queue, i)

    return result

print(bfs())
