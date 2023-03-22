# 위상정렬
# 분류 accepted

# 답이 여러가지일 경우, 아무거나 출력한다 -> 위상정렬 힌트!
# 나를 가르키고 있는 노드가 없으면 그 상태에서는 내가 가장 크다.
# 나랑 연결된 노드들은 나보다 작은 노드들이다.
# 연결 여부 check가 중요!!!!
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().rstrip().split())

# 단방향 연결
adj = [[] for _ in range(N+1)]

# 진입차수, 날 가르키고 있는 노드
indegree = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    adj[a].append(b) # a → b
    indegree[b] += 1 # b를 가르키고 있는 노드 a가 있으므로 indegree[b]에 cnt ++

def topology_sort():
    # 생성
    q = deque()
    result = []

    for i in range(1, N+1):
        if indegree[i] == 0: # 나를 가르키고 있는 노드가 없다면?
            q.append(i)
    
    while q:
        cur_n = q.popleft()
        result.append(cur_n)
        for next_n in adj[cur_n]:
            indegree[next_n] -= 1 # 현재 노드와 연결된 노드들의 차수를 감소
            if indegree[next_n] == 0:
                q.append(next_n)
    return result

answer = topology_sort()
print(*answer)