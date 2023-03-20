# 그래프의 모든 정점들을 연결하는 부분 그래프 중, 
# 가중치의 합이 최소인 트리
# 사이클이 있어서 안됨. 
# 따라서, n개의 정점을 n-1개의 간선으로 연결

"""
정점 최대 10000개,
10000개이므로, O(n^2)이상의 알고리즘 X
=> prim : O(N^2) -> ㄴㄴ

Kruskal
1. 주어진 모든 간선 비용이 낮은(오름차순)로 정렬
2. 정렬된 간선 확인하면서 간선이 노드들 간 사이클 발생시키는지 확인
3. 사이클 발생하지 않으면 최소 신장트리에 포함, 발생하면 포함X
4. 1~3을 모든 간선에 대해 반복 수행

사이클 발생은 노드들의 부모노드가 같은지에 따라 확인
ㄴ 부모테이블 있어야 함
"""
import sys

input = sys.stdin.readline

v, e = map(int, input().split()) # 정점개수, 간선개수

# 간선정보 받아서 비용 기준 오름차순 정렬
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b)) # a와 b가 가중치 c로 연결돼 있음
edges.sort()

parent = [0] * (v+1)
# 인덱스 = 정점
for i in range(1, v+1):
    parent[i] = i

# find연산
def find(parent, cur):
    if parent[cur] != cur:
        parent[cur] = find(parent, parent[cur])
    return parent[cur]

# union 연산
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b 

# 전체 가중치
res = 0

for i in range(e):
    cost, a, b = edges[i]

    # 부모가 같은지 확인하고, 다르면 union 연산 수행
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        res += cost

print(res)




