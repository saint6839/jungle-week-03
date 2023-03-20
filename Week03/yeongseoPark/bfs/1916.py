"""
n이 1000개라 found배열로 방문정점 표시하면 100만 연산 -> 1초 넘을것 같음

최소힙으로 다익스트라 구현

a ~ b가는 최소비용 출력
"""
import sys 
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())

    graph[a].append((cost, b)) # 비용, 도착지 

start, end = map(int, input().split())

distance = [sys.maxsize] * (n+1)
heap = [] 

heappush(heap, (0, start))
distance[start] = 0

while heap:
    cost, vertex = heappop(heap) # vertex까지 가는 최소비용, vertex

    if cost > distance[vertex]: # 최소비용 갱신할 수 없기때문에 볼 필요없음, 시간 초과 방지
        continue

    for i in graph[vertex]:
        weight = i[0]
        arrival  = i[1]

        if weight + cost < distance[i[1]]: # vertext 거쳐서 i[1]로 가는게 현재 distance배열에 기록된 최소거리보다 짧으면
            distance[i[1]] = weight + cost
            heappush(heap, (weight+cost, arrival))

print(distance[end])
        


