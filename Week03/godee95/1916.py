# 분류 : fail

# Dijkstra Algorithm 다익스트라 알고리즘
# 가장 짧은 경로를 찾는 알고리즘
# 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복
# 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 선택!

import heapq
from sys import maxsize
import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

bus = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, input().rstrip().split())

    bus[a].append((cost, b))

start, end = map(int, input().rstrip().split())

# 방문 표시
visited = [maxsize] * (N+1) # heap 자료구조를 사용하기 위해 최댓값으로 설정

def dijkstra(node):
    pq = []
    heapq.heappush(pq, (0, node)) # 비용 0, 방문도시 node
    visited[node] = 0

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if visited[cur_node] < cur_cost:
            continue

        for next_cost, next_node in bus[cur_node]:
            sum_cost = cur_cost + next_cost
            if visited[next_node] > sum_cost:
                heapq.heappush(pq, (sum_cost, next_node))
                visited[next_node] = sum_cost

dijkstra(start)
print(visited[end])