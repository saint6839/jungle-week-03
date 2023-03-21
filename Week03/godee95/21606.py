# 분류 : fail

# 참고 자료1 : https://velog.io/@tmdejr1117/SW%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90-%EC%A0%95%EA%B8%8023%EC%9D%BC%EC%B0%A8-TIL-%EB%B0%B1%EC%A4%80-21606-%EC%95%84%EC%B9%A8-%EC%82%B0%EC%B1%85%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 참고 자료2 : https://woonys.tistory.com/entry/%EC%A0%95%EA%B8%80%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90-22%EC%9D%BC%EC%B0%A8-TIL-%EC%95%84%EC%B9%A8-%EC%82%B0%EC%B1%85with-Python-%EC%9C%84%EC%83%81-%EC%A0%95%EB%A0%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

import sys
input = sys.stdin.readline

N = int(input().rstrip())
# index를 노드로 의미하게 하기 위해

answer = 0
location =[0]+list(map(int, input().strip()))
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().rstrip().split(' '))
    adj[a].append(b)
    adj[b].append(a)
    # 둘 다 실내일 경우 
    if location[a] == 1 and location[b] == 1:
        answer += 2

# 그래프를 돌면서 인접노드가 실내이면 cnt++
# 인접노드가 실외이면 그 정점에서 dfs로 다시 탐색!
# 우리가 필요한 정보는 실내 갯수!
def dfs_indoors_cnt(node, cnt):
    visited[node] = True

    for next_node in adj[node]:
        if location[next_node] == 1: # 실내 일때, 방문여부 표현 안해도 됨!
            cnt += 1
        elif not visited[next_node] and location[next_node] == 0: # 방문하지 않았고 실외이면.
            visited[next_node] = True
            dfs_indoors_cnt(next_node, cnt)
    return cnt

# 경로
course = answer

# 방문표시
visited = [False]*(N+1)

# 모든 노드를 다 방문
for i in range(1, N+1):
    if not visited[i] and location[i] == 0:
        x = dfs_indoors_cnt(i, 0)
        course += x * (x-1)

print(course)