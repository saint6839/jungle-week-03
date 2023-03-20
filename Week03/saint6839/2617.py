import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())

bigger_than_index = [[] for _ in range(N+1)]
smaller_than_index = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    bigger_than_index[a].append(b)
    smaller_than_index[b].append(a)

mid = (N+1) / 2

def dfs(arr, n):
    global count
    for i in arr[n]:
        if not visited[i]:
            visited[i] = True
            count += 1
            dfs(arr, i)

answer = 0
for i in range(1, N+1):
    visited = [False for _ in range(N+1)]
    count = 0
    dfs(bigger_than_index, i)
    if count >= mid:
        answer += 1
    count = 0
    visited = [False for _ in range(N+1)]
    dfs(smaller_than_index, i)
    if count >= mid:
        answer += 1

print(answer)

