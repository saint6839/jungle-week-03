"""
다익스트라를 하면서 distance배열 업데이트해줄때마다 현재 위치에서의 색깔을 확인
검은색이면 ans + 1 해주기
"""
import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, list(input().strip()))) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

heap = []
heappush(heap, (0,0,0)) # 비용, row, col

while heap:
    cost, row, col = heappop(heap)

    if row == n-1 and col == n-1:
        break

    for i in range(4):
        newR = row + dr[i]
        newC = col + dc[i]

        if 0 <= newR < n and 0 <= newC < n and not visited[newR][newC]:
            visited[newR][newC] = True 
            if matrix[newR][newC] == 0: # 검은방을 지나면 비용을 증가
                heappush(heap, (cost+1, newR, newC)) # 
            else:
                heappush(heap, (cost, newR, newC))

print(cost)





