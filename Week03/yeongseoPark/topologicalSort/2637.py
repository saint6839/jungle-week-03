"""
기본부품, 중간부품 -> 중간부품

기본부품, 중간부품 -> 완제품

하나의 완제품 조립하기 위해서 필요한 "기본부품의 종류별 개수"
"""
from collections import deque
import sys

input = sys.stdin.readline

n = int(input()) # 1 ~ n-1 은 기본 부품 OR 중간부품, n은 완제품
m = int(input())

graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)

for _ in range(m):
    x, y, k = map(int, input().split())

    graph[y].append((x, k)) # y에서 x로 갈때 cost가 k

    in_degree[x] += 1

q = deque()

for i in range(1, n+1):
    if in_degree[i] == 0:
        q.append(i) # 기본부품들 큐에 삽입

needs = [[0] * (n+1) for _ in range(n+1)] # needs배열에 필요한 부품들의 개수 기록

while q:
    now = q.pop()

    for next, cost in graph[now]:
        if needs[now].count(0) == n+1: # 현재것이 기본부품이면
            needs[next][now] += cost
        
        else: # 현재것이 중간부품이면 
            for i in range(1, n+1):
                needs[next][i] += needs[now][i] * cost
        
        in_degree[next] -= 1

        if in_degree[next] == 0:
            q.append(next)

for i in range(1,n+1):
    if needs[n][i] != 0:
        print(str(i) + " " + str(needs[n][i]))

