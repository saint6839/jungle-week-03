import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
reversed_graph = [[] for _ in range(N+1)]
in_degree = [0 for _ in range(N+1)]

for _ in range(M):
    a, b, cost =  map(int, sys.stdin.readline().split())
    graph[a].append([b, cost])
    reversed_graph[b].append([a, cost])
    in_degree[b] += 1

start, end = map(int, sys.stdin.readline().split())

queue = deque()
queue.append(start)

costs = [0 for _ in range(N+1)]
ways = set()

while queue:
    popped = queue.popleft()
    for next, cost in graph[popped]:
        costs[next] = max(costs[next], costs[popped] + cost)
        in_degree[next] -= 1
        if not in_degree[next]:
            queue.append(next)

visited = [False for _ in range(N+1)]

count = 0
queue.append(end)
while queue:
    popped = queue.popleft()
    for before, cost in reversed_graph[popped]:
        if costs[popped] == costs[before] + cost:
            count += 1
            if not visited[before]:
                visited[before] = True
                queue.append(before)

print(costs[end])
print(count)

