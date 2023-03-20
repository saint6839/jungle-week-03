# 1번 노드와 연결된 노드의 수를 출력하는 프로그램

# 입력받고
import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

# 각 노드와 연결 요소 알려주는 리스트
adj = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    adj[a].append(b)
    adj[b].append(a)

# 방문 표시
visited = [False]*(N+1)

# 탐색 코드 구현
def DFS(node):
    visited[node] = True

    for next_node in adj[node]:
        if visited[next_node] == False:
            visited[next_node] = True
            DFS(next_node)

# 바이러스 걸린 1번 컴퓨터와 연결된 노드 탐색
DFS(1)

# 1번 컴퓨터와 연결된 노드 cnt, 자기 자신은 제외
print(visited.count(True) - 1)