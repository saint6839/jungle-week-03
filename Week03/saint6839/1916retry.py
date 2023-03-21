import heapq
import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append([cost, b])

A, B = map(int ,sys.stdin.readline().split())

costs = [sys.maxsize for _ in range(N + 1)]

min = sys.maxsize
def bfs(start, cost):
    global B, min
    queue = []
    heapq.heappush(queue, [cost, start])

    while queue:
        popped = heapq.heappop(queue)
        p_start = popped[1]
        p_total_cost = popped[0]
        if costs[p_start] < p_total_cost:
            continue

        for i in graph[p_start]:
            if costs[i[1]] > p_total_cost + i[0]:
                costs[i[1]] = p_total_cost + i[0]
                heapq.heappush(queue, [p_total_cost + i[0], i[1]])

bfs(A, 0)
print(costs[B])
