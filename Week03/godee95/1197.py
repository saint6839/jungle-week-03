# 분류 : fail

# 1197 최소스패닝트리

# 참고 영상 : https://youtu.be/Gj7s-Nrt1xE

# 최소스패닝트리 관련 문제
# https://www.acmicpc.net/problem/4386
# https://www.acmicpc.net/problem/1774
# https://www.acmicpc.net/problem/2887
# https://www.acmicpc.net/problem/6091
# https://www.acmicpc.net/problem/1626
# https://www.acmicpc.net/problem/16213
# https://www.acmicpc.net/problem/1647
# https://www.acmicpc.net/problem/15481

# -----------------------------------------------------------
# 최소 스패닝 트리(Minimum Spannig Tree)
# 크루스칼 알고리즘(Kruskal's Algorithm)

# import sys
# input = sys.stdin.readline

# # Disjoint-set 서로소 집합 find-Union

# # 특정 원소가 속한 집합 찾기 find
# def find_parent(parent, x):
#     # 루트 노드를 찾을 때 까지 재귀 호출
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# # Union
# # 이 코드 잘 이해 안됨... 이게 왜 합치기임???
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# # 입력
# v, e = map(int, input().rstrip().split())

# # 부모테이블 초기화
# parent = [0]*(v+1)

# # 부모 테이블상에서 부모를 자기 자신으로 초기화
# for i in range(1, v+1):
#     parent[i] = i

# edges = []
# for _ in range(e):
#     a, b, cost = map(int, input().rstrip().split())
#     edges.append((cost, a, b))

# # 1. 간선 데이터를 비용에 따라 오름차순으로 정렬합니다.
# # 비용이 첫번째 원소임으로~
# edges.sort()


# # print(find_parent(parent, 2))

# # 2. 간선을 하나씩 확인하며 현재 간선이 사이클을 발생시키는지 확인
# # 2-1. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
# # 2-2. 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않습니다.
# # 3. 모든 간선에 대하여 2번 과정을 반복합니다.
# result = 0 # 최종 비용을 담을 변수
# for edge in edges:
#     cost, a, b = edge
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost

# # 출력
# print(result)

# ------------------------------------------------------------
# 프림 알고리즘(Prim Algorithm)

import sys
import heapq
input = sys.stdin.readline

def BOJ1197() :
  V, E = map(int, input().split())
  
  graph = [[] for _ in range(V+1)]
  visited = [False for _ in range(V+1)]

  for _ in range(E) :
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

  def prim() :
    result = 0
    queue = []
    queue.append([0, 1])

    while queue :
      curr_cost, curr_node = heapq.heappop(queue)
      if visited[curr_node] == False :
        visited[curr_node] = True
        result += curr_cost
        for next_node, next_cost in graph[curr_node] :
          heapq.heappush(queue, (next_cost, next_node))
          
    return result 

  print(prim())

BOJ1197()