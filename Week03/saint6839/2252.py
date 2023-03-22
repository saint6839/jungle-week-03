import heapq
import sys

N, M = map(int, sys.stdin.readline().split())


graph = [[] for _ in range(N+1)]
in_degree = [0 for _ in range(N+1)]



for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    in_degree[b] += 1

priority_queue = []
results = []

for i in range(1, N+1):
    if not in_degree[i]:
        heapq.heappush(priority_queue, i)

while priority_queue:
    temp = heapq.heappop(priority_queue)
    results.append(temp)
    for i in graph[temp]:
        in_degree[i] -= 1
        if not in_degree[i]:
            heapq.heappush(priority_queue, i)

print(*results)