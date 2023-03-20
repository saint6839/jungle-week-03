
"""
위상정렬하면서, 순서 어긋난거 있으면 서로 바꿔주는 식으로 계속하다가,
더이상 바꿀거 없으면 그래프 리턴하게 했는데 실패
"""
# import sys
# from heapq import heappush, heappop
# # from collections import deque
# input = sys.stdin.readline

# n = int(input())

# graph = [[-1] for _ in range(n+1)]
# in_degree = [0] * (n+1) 

# for i in range(1, n+1):
#     tmp = list(map(int,list(input().strip())))

#     for j in range(n):
#         if tmp[j] == 1:
#             in_degree[j+1] += 1

#     graph[i] += tmp

# q = [] 

# for i in range(1, n+1):
#     if in_degree[i] == 0:
#         heappush(q, i)

# def topo():
#     cnt = 0 
#     while q:
#         now = heappop(q)
#         cnt += 1

#         changed = False

#         for i in range(1, n+1):
#             if graph[now][i] == 1:
#                 if now < i:
#                     in_degree[i] -= 1
#                     if in_degree[i] == 0:
#                         heappush(q, i)

#                 else: # now랑 i랑 자리바꿔야함
#                     graph[now][i] = 0
#                     graph[i][now] = 1
#                     changed = True
#                     in_degree[now], in_degree[i] = in_degree[i], in_degree[now]
#                     in_degree[now] -= 1
#                     if in_degree[now] == 0:
#                         heappush(q, now)
        
                    
#         # 모든 곳을 위상정렬로 방문하기전에 끝남- > 사이클 존재
#     if len(q) == 0 and cnt < n-1:
#         print(-1)
#         exit()
    
#     return changed

# while True:
#     res = []
#     if not topo():
#         break

"""
https://velog.io/@whddn0221/%EB%B0%B1%EC%A4%80-1432-%EA%B7%B8%EB%9E%98%ED%94%84-%EC%88%98%EC%A0%95-%EC%9C%84%EC%83%81%EC%A0%95%EB%A0%AC-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90-mrltwcp5
https://wonyoung2257.tistory.com/80
현재의 그래프를 "위상정렬해서 1,2,3,... n이 나오게" 바꾸면 됨
- 이러기 위해서는
1. 진입차수가 0인 노드부터 시작해서 쭉 거슬러 올라가면
2. 진출차수가 0인 노드를 만나게 되고, 이 노드가 가장 큰 노드다
=> 따라서 위상정렬로
    초기에 진출차수가 0 인 정점에 가장 큰 수를 넣고'
    해당 정점과 연결된 정점들의 진출차수를 1씩 빼면서
    그 과정에서 진출차수가 0인 정점을 큐에 넣는 과정을 반복하며
    큰 수부터 차례대로 작은 수를 result 리스트에 저장

=> 위상정렬 결과가 오름차순이 나오게 하기 위해서, 현재 그래프에 대해서 진출차수 기준으로 위상정렬을 하며 큰 숫자(정점값)부터 집어넣는 것 

근데 위의 위상정렬 과정에서 큐에 0인게 여러개 들어 있을 수 있잖아?
근데 우리가 원하는 것은 사전순 출력이고, 현재 큰 값부터 정점에 넣어주고 있으니까
진출차수가 0인개 여러개면, 큰 값이 뒤로가야 오름차순이 되니깐,
최대힙을 사용해 인덱스가 큰 노드에 큰 값이 들어가게 해줌
"""
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

outdegree = [0] * (n+1) # 진출차수

result = [0] * (n+1)

# 진입차수가 아닌 진출차수를 잰다
for i in range(1, n+1):
    con = list(map(int, input().strip()))

    for idx, val in enumerate(con):
        if val == 1: 
            # 인덱스번호의 정점에 들어오는 정점들을 저장 - idx+1로 들어오는 것들 -> 진출차수 기준 위상정렬이기에
            # 인접 리스트에는 자신한테 "들어오는" 값들을 저장해야 함 - 그래야 진출차수 없애면서 자신에 해당하는 애들을 없앨 수 있다 
            graph[idx + 1].append(i) 
            outdegree[i] += 1  # 이거는 i에서 나가는 차수(진출차수)

def topology(n):
    heap = [] # 인덱스 큰 노드 먼저 큐에서 빼기 위해 우선순위큐(사전순 앞서는것)

    for i in range(1, n+1):
        if outdegree[i] == 0:
            heappush(heap, -i)  # 최대힙
    
    while heap:
        now = -heappop(heap) 
        result[now] = n 

        for shooting_node in graph[now]:
            outdegree[shooting_node] -= 1 # now로 쏘는 노드들의 진출차수 감소시킴 
            if outdegree[shooting_node] == 0:
                heappush(heap, -shooting_node)

        n -= 1

topology(n)

# 사이클 형성, 따라서 그래프 번호를 수정할수 없는게 세개이상
if result.count(0) > 2:
    print(-1)
else:
    print(''.join(map(str, result[1:])))


