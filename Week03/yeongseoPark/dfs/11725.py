"""
간선들이 주어짐, 이거는 트린데
트리의 루트가 1

2번 노드부터 n번노드까지 부모를 출력

1부터 dfs를 하는데, 다음 탐색 노드의 번호에 대한 부모로 앞전(지금 현재 함수의 값) 값을 기록
이건 parents배열 만들면 될듯
"""

import sys

# 노드의 개수 10만개니까 recursion제한 풀어줌 
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n = int(input())

dic = {i: [] for i in range(1, n+1)}

for _ in range(n-1):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

parents = [0] * (n+1)
visited = [0] * (n+1)

def dfs(cur):
    visited[cur] = True

    for i in dic[cur]:
        if not visited[i]:
            parents[i] = cur
            dfs(i) 

dfs(1)
for i in range(2, n+1):
    print(parents[i])