"""
1 ~ N 구슬
무게 순서로 (N+1) // 2번째 찾기
M = N(N-1) // 2 의 쌍을 저울에 올려서 뭐가 더 무거운지 모두 알아냄(쌍의 순서는 상관X)

무게가 절대로 중간이 될 수 없는 구슬의 개수 

구슬이 정점, 쌍이 간선(방향 그래프) 라고 생각

특정 정점에서 가거나 , 특정 정점으로 올 수 있는 개수가 (n+1) // 2 개 이상이면, 
적어도 내 위나 아래로 그만큼 있고, 나는 (n+1)//2 보다 작거나 클테니까, 후보군에서 제외됨

가는거는 셀 수 있는데 
오는거는 딕셔너리에 따로 기록을 해야할듯


n이 99개밖에 안되니깐 시간적 제약이 없을거임
"""
import sys

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)] 
graph_reversed = [[] for _ in range(n+1)] # 뒤집어서(이번엔 나보다 큰애들)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b) 
    graph_reversed[b].append(a)


# dfs를 타다가 cnt가 기준을 넘으면 false를 반환
# 넘기전에 끝나면 그냥 끝
def dfs(start, graph):
    global cnt
    cnt += 1

    for i in graph[start]:
        if not visited[i]:
            visited[i] = True 
            dfs(i, graph)

standard = (n-1) // 2 
answer = 0 

for i in range(1, n+1):
    visited = [False] * (n+1)
    cnt = -1
    dfs(i, graph)
    if cnt > standard:
        answer += 1
    
    cnt = -1
    dfs(i, graph_reversed)
    if cnt > standard:
        answer += 1

print(answer)


