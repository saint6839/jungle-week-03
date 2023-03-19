# 분류 : accepted

# 입력받고
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

# node 연결 양방향 연결관계
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    adj[a].append(b)
    adj[b].append(a)

# 솔루션
# 방문 표시
visited = [False]*(N+1)

# 탐색 함수 만들기
def DFS(node):
    visited[node] == True # 해당 노드 방문했다고 표시
    for next_node in adj[node]: # 해당 노드와 인접한 노드들 돌면서
        if visited[next_node] == False: # 방문한 적 없으면
            visited[next_node] = True # 방문 표시하고
            DFS(next_node) # 탐색

cnt = 0
# 모든 노드를 돌면서 해당 노드 방문한 적없으면, 탐색 시작!
# 연결되어 있을 경우에만, 방문하지 않은 경우에만 dfs 들어가도록 코드 구현!
for node in range(1, N+1):
    if visited[node] == False: # 이 줄 중요!
        visited[node] = True
        DFS(node)
        cnt += 1

# 출력
print(cnt)