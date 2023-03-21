import sys

N, M = map(int, sys.stdin.readline().split())

smaller_than_index = [[] for _ in range(N + 1)]
bigger_than_index = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    smaller_than_index[a].append(b)
    bigger_than_index[b].append(a)

def small_dfs(start):
    global count

    for i in smaller_than_index[start]:
        if not visited[i]:
            visited[i] = True
            count += 1
            small_dfs(i)

def big_dfs(start):
    global count

    for i in bigger_than_index[start]:
        if not visited[i]:
            visited[i] = True
            count += 1
            big_dfs(i)

result = 0
for i in range(1, N+1):
    visited = [False for _ in range(N+1)]
    count = 0
    small_dfs(i)
    if count >= (N+1)/2:
        result += 1

    visited = [False for _ in range(N + 1)]
    count = 0
    big_dfs(i)
    if count >= (N+1)/2:
        result += 1

print(result)
