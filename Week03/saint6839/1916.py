import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append([b, cost])

A, B = map(int ,sys.stdin.readline().split())

queue = deque()

min = sys.maxsize
def bfs(start, cost):
    global B, min

    queue.append([start, cost])

    while queue:
        popped = queue.popleft()
        p_start = popped[0]
        p_total_cost = popped[1]
        for i in graph[popped[0]]:
            queue.append([i[0], p_total_cost + i[1]])
        if p_start == B:
            if min > p_total_cost:
                min = p_total_cost

bfs(A, 0)
print(min)
