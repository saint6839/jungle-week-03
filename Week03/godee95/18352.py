# 반례
# 2 2 2 1
# 1 2
# 2 1
# answer : -1
# visited를 0으로 초기화 했을 때 결과 1

import sys
input = sys.stdin.readline
from collections import deque

N, M, K, X = map(int, input().rstrip().split(' '))

adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().rstrip().split(' '))
    adj[a].append(b)

visited = [-1]*(N+1) # 방문표시
# visited를 0으로 초기화면 시작점을 다시 방문하게 됨. 그렇게 때문에 -1로 초기화 해줘야 함!!

def BFS(node):
    # 생성
    q = deque()
    q.append(node)

    while q:
        cur_node = q.popleft()
        for next_node in adj[cur_node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[cur_node] + 1
                q.append(next_node)

visited[X] = 0
BFS(X)

if visited.count(K) == 0:
    print(-1)
else:
    for i in range(1, N+1):
        if visited[i] == K:
            print(i)
