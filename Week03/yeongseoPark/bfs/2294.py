"""
n종류의 동전, 가치의 합이 k
동전의 개수는 최소
각각 동전은 여러개 사용 가능
순서는 상관없고 구성만 같으면 하나의 경우
"""
import sys
from collections import deque 

input = sys.stdin.readline

n, k = map(int, input().split())

minVal = sys.maxsize

coin = [int(input()) for _ in range(n)]

# # 힙 말고 큐 사용
def bfs():
    minVal = sys.maxsize
    visit = [False] * 10001 # 같은 sum이 여러개 큐에 들어가는 것을 방지
    # 방지해주지 않으면 메모리초과 나게됨

    que = deque()

    que.append((0, 0)) # 개수, 총합

    while que:
        poped = que.pop()

        for i in coin:
            if poped[1] + i == k:
                minVal = min(minVal ,poped[0] + 1)
            
            if poped[1] + i > k:
                continue
            
            if visit[poped[1] + i] == False:
                que.appendleft((poped[0] + 1, poped[1] + i))
                visit[poped[1] + i] = True
    
    if minVal == sys.maxsize:
        print(-1)
    else:
        print(minVal)
            
bfs()
    

""" 
dfs 풀이 -> 안됨
"""
# visited = [False] * 10001
# minVal = sys.maxsize
# def dfs(idx, cnt, summ):
#     global minVal

#     if summ > k or cnt >= minVal:
#         return

#     if summ == k:
#         minVal = min(minVal, cnt)
#         return
    
#     visited[summ] = True
    
#     for i in range(idx, n):
#         if not visited[summ + coin[i]]:
#             dfs(i, cnt + 1, summ + coin[i])

# dfs(0, 0, 0)
# print(minVal)


