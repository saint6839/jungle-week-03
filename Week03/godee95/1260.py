# 분류 : accepted

# DFS와 BFS
# 참고 영상 : https://youtu.be/kkZFEwoZ3fA

# 간선 양방향 adj
# 출력 ans_dfs, ans_bfs

# 입력받고
import sys
input = sys.stdin.readline

from collections import deque

N, M, V = map(int, input().rstrip().split())

# 인덱스를 노드 번호롤 쓰니깐! 0번 인덱스는 불필요
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    adj[a].append(b)
    adj[b].append(a)

# 정점 작은 순으로 오름차순 정렬
for list in adj:
    list.sort()

# 솔루션 함수
ans_dfs = []
def dfs(node):
    visited[node] = True
    ans_dfs.append(node)
    for next_node in adj[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node)

dq = deque()
ans_bfs = []
def bfs(start):
    visited[start] = True
    ans_bfs.append(start)
    dq.append(start)

    while dq:
        node = dq.popleft()
        for next_node in adj[node]:
            if not visited[next_node]:
                visited[next_node] = True
                dq.append(next_node)
                ans_bfs.append(next_node)

visited = [False]*(N+1) 
dfs(V)

visited = [False]*(N+1) 
bfs(V)

print(*ans_dfs)
print(' '.join(map(str, ans_bfs)))
# print(*ans_bfs)