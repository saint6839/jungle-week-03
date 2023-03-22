import heapq
import sys

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
in_degree = [0 for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    in_degree[B] += 1

priority_queue = []
for i in range(1, N+1):
    if not in_degree[i]:
        heapq.heappush(priority_queue, i)

results = []

while priority_queue:
    popped = heapq.heappop(priority_queue)
    results.append(popped)

    for i in graph[popped]:
        in_degree[i] -= 1
        if not in_degree[i]:
            heapq.heappush(priority_queue, i)

print(in_degree)

print(*results)