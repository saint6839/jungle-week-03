import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

in_degree= [0] * (n+1) # 진입차수 
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b) # a -> b

    in_degree[b] += 1 # b로의 진입차수 1증가

def topology():
    q = deque()

    for i in range(1, n+1):
        if in_degree[i] == 0: # 진입차수가 0인애들부터 큐에 넣음
            q.append(i)
    
    while q:
        poped = q.pop() 
        print(poped, end=" ")

        for i in graph[poped]:
            # 방금 위상정렬로 출력한 곳에서 갈 수 있는 정점들의 진입차수 1 감소
            in_degree[i] -= 1

            if in_degree[i] == 0:
                q.append(i)

topology()





