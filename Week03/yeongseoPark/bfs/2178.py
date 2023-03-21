import sys
from collections import deque 

input = sys.stdin.readline

n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append([int(i) for i in input().strip()])

# 남 동 북 서 
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs(row, col):
    deq = deque()

    deq.append((row,col))

    cnt = 0

    visited = [[0] * m for _ in range(n)]

    while deq:
        cnt += 1
        cur = deq.pop()
        visited[cur[0]][cur[1]] = True

        for i in range(4):
            newR = cur[0] + dr[i]
            newC = cur[1] + dc[i]

            if 0 <= newR < n and 0 <= newC < m and not visited[newR][newC] and matrix[newR][newC] == 1:
                deq.appendleft((newR, newC))
                matrix[newR][newC] += matrix[cur[0]][cur[1]]
    
bfs(0,0)
print(matrix[n-1][m-1])
    

        

        


