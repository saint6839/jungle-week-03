import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
reverse_graph = [[] for _ in range(N+1)]

in_degree = [0 for _ in range(N+1)]
result = [0 for _ in range(N+1)]

for _ in range(M):
    x, y, cost = map(int, sys.stdin.readline().split())
    graph[x].append([y, cost])
    reverse_graph[y].append([x, cost])
    in_degree[y] += 1

start, end = map(int, sys.stdin.readline().split())

queue = deque()
queue.append(start)

while queue:
    popped = queue.popleft()
    for next, cost in graph[popped]:
        result[next] = max(result[next], result[popped] + cost)
        in_degree[next] -= 1
        if in_degree[next] == 0:
            queue.append(next)

queue.append(end)

count = 0
visited = [False for _ in range(N+1)]

while queue:
    popped = queue.popleft()
    for before, cost in reverse_graph[popped]:
        if result[popped] == result[before] + cost:
            count += 1
            if not visited[before]:
                queue.append(before)
                visited[before] = True

print(result[end])
print(count)
