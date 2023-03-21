"""
정점 N개, 간선 M개, 단방향 그래프

특정도시 X ~ 모든 도시 중, 최단 거리 정확히 K인 도시들의 번호
"""
# 입력받기 
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

# weight : 인접 행렬 -> 메모리초과, 인접 리스트로
weight = [[] for _ in range(n+1)]
# 시작 정점에서 s에 있는 정점만을 거쳐서 다른 정점으로 가는 최단거리 기록하는 배열
distance = [sys.maxsize] * (n+1) 
heap = []

for _ in range(m):
    a, b = map(int, input().split())
    weight[a].append([b,1])  # 정점, 가중치

def shortest_path(start):
    heappush(heap, [0, start])
    distance[start] = 0 
    while heap:
        w, n = heappop(heap) # 힙에서  distance가장 작은 것 꺼냄 / 거리, 정점

        # distance값이 가장 짧은 것을 꺼냈기 때문에, 
        # 알고리즘에서 처리한 적 없다면, 다른 경로보다 길수가 없음,
        # 제일 짧은 거리 < 덜 짧은거리1 + 덜짧은거리2 일 테니까
        # 따라서 꺼낸 가중치가 distance배열의 값보다 크다면, 이미 처리돼서 더 볼 필요없음
        if distance[n] < w:
            continue 

        for v, wei in weight[n]: # 
            n_w = wei + w
            if n_w < distance[v]:
                distance[v] = n_w
                heappush(heap, [n_w, v])

shortest_path(x)
printed = False 
for i in range(len(distance)):
    if distance[i] == k:
        printed= True 
        print(i)

if not printed:
    print(-1)
    


# # 방문집합에 속하지 않는 정점 중 최소 distance 가진 정점
# def choose(distance, n, found):
#     minVal = sys.maxsize
#     minPos = -1

#     for i in range(1, n+1):
#         if distance[i] < minVal and not found[i]:
#             minVal = distance[i]
#             minPos = i
    
#     return minPos
