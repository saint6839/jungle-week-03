# 입력 받고
import sys
sys.setrecursionlimit(10**9) # dfs 런타임에러 발생해서 추가한 코드!
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())

adj = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().rstrip().split(' '))
    adj[a].append(b)
    adj[b].append(a)

# 부모노드 입력 및 방문표시
# 방문 안했다면 0, 했다면 어떤 부모노드로 부터 들어온 것 인지 기록남기기
visited = [False] * (N+1)
parent = [0] * (N+1)

def DFS(node):
    # visited[node] = True

    for next_node in adj[node]:
        if visited[next_node] == False: # 방문한 적 없다면
            visited[next_node] = True 
            parent[next_node] = node # 부모노드가 무엇인지 기록
            DFS(next_node)

visited[1] = True
DFS(1) # root node인 1부터 탐색 시작

for i in range(2, N+1):
    print(str(parent[i]) + "\n")

# --------------------------- BFS로 구현 ------------------------------

import sys
input = sys.stdin.readline
from collections import deque

N = int(input().rstrip())

adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().rstrip().split(' '))
    adj[a].append(b)
    adj[b].append(a)

# 방문 표시
visited = [False] * (N+1)

# 인접노드 저장할 큐
dq = deque()

# 부모 노드를 저장할 리스트
parent = [0]*(N+1)

# 탐색 함수 구현
def BFS(node):
    dq.append(node)

    while dq:
        cur_node = dq.popleft()
        for next_node in adj[cur_node]:
            if visited[next_node] == False:
                visited[next_node] = True
                parent[next_node] = cur_node # 부모노드 저장
                dq.append(next_node)

# BFS는 한번만 돌고 다시 자기 호출 안함!
BFS(1) # 루트 노드 1부터 탐색 시작

print('\n'.join(map(str, parent[2:])))