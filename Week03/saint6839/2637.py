import sys
from collections import defaultdict, deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())


graph = [[] for _ in range(N+1)]
in_degree = [0 for _ in range(N+1)]
results = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    X, Y, K = map(int, sys.stdin.readline().split())
    graph[Y].append([X, K])
    in_degree[X] += 1

queue = deque()
base_items = []
for i in range(1, N+1):
    if in_degree[i] == 0:
        queue.append(i)
        base_items.append(i)

def bfs():
    while queue:
        popped = queue.popleft()
        for target, need in graph[popped]:
            if popped in base_items:
                results[target][popped] += need
            else:
                for i in range(1, N+1):
                    results[target][i] += results[popped][i] * need
                    print(*results, sep='\n')
                    print()

            in_degree[target] -= 1
            if in_degree[target] == 0:
                queue.append(target)

bfs()

for result in enumerate(results[N]):
    if result[1] > 0:
        print(*result)


