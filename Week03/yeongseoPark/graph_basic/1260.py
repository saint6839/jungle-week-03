"""
그래프 , DFS와 BFS 탐색 결과
간선은 양방향, 정점 사이 간선 여러개 가능
방문 가능한 정점 여러개일시 번호 작은것부터
- DFS의 경우 정점 번호순 오름차순 정렬
- BFS도 오름차순 정렬해놓고 큐에 넣으면..? 
더이상 방문 불가능이면 종료 
정점번호 1~N
"""
from collections import deque
import sys

input = sys.stdin.readline

n , m, v = map(int, input().split())

dic = {}
for i in range(1, n+1):
    dic[i] = []

for _ in range(m):
    a, b   = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

# 정점 번호기준 오름차순 정렬
for i in range(1, n+1):
    dic[i].sort()

dfs_res = []
visited = [0] * (n + 1)
def dfs(cur):
    dfs_res.append(cur)
    visited[cur] = 1
    for i in dic[cur]:
        if not visited[i]:
            dfs(i)

bfs_res = []
visited_bfs = [0] * (n+1)
que = deque()
que.append(v)
visited_bfs[v] = 1

while que:
    visit = que.pop() 
    bfs_res.append(visit) 

    for i in dic[visit]:
        if not visited_bfs[i]:
            visited_bfs[i] = 1 
            # 큐에 넣는 즉시 방문처리 해줘야, 큐에서 해당 노드 나오기 전에 또 추가되는 것 막음
            que.appendleft(i)

dfs(v)
for i in dfs_res:
    print(i, end=" ")

print()
for i in bfs_res:
    print(i, end=" ")

   



 