"""
그냥 dfs 해서 개수 구하면 될듯
"""

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

dic = {}
for i in range(1, n+1):
    dic[i] = []

for _ in range(m):
    a, b= map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

visited = [0] * (n+1)
ans = 0 
def dfs(vtx):
    global ans
    ans += 1
    visited[vtx] = True 
    for i in dic[vtx]:
        if not visited[i]:
            dfs(i)

dfs(1)     
print(ans-1)
    

