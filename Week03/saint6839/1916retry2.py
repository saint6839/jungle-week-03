import heapq
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())


graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append([cost, b])

start, end = map(int, sys.stdin.readline().split())

visited = [False for _ in range(N+1)]

costs = [sys.maxsize for _ in range(N+1)]

# print(graph)
min = sys.maxsize
def bfs(start):
    global min

    priority_queue = []
    heapq.heappush(priority_queue, [0, start])

    while priority_queue:
        pcost, ps = heapq.heappop(priority_queue)
        if costs[ps] < pcost:
            continue

        for i in graph[ps]:
            if costs[i[1]] > pcost + i[0]:
                costs[i[1]] = pcost + i[0]
                heapq.heappush(priority_queue, [pcost + i[0], i[1]])

bfs(start)
print(costs[end])