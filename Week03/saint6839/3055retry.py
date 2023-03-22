import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())

board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

startX = 0
startY = 0

endX = 0
endY = 0

queue = deque()

for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':
            queue.append([i, j, 0])

for i in range(R):
    for j in range(C):
        if board[i][j] == '*':
            queue.append([i, j, 0])
        if board[i][j] == 'D':
            endX = i
            endY = j

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while queue:
    px, py, pcost = queue.popleft()

    for i in range(4):
        nx = px + dx[i]
        ny = py + dy[i]
        if 0 <= nx < R and 0 <= ny < C :
            if board[px][py] == 'S' and (board[nx][ny] == '.' or board[nx][ny] == 'D'):
                if board[nx][ny] == 'D':
                    print(pcost + 1)
                    sys.exit(0)

                board[nx][ny] = 'S'
                queue.append([nx, ny, pcost + 1])
            if board[px][py] == '*' and (board[nx][ny] == '.' or board[nx][ny] == 'S'):
                board[nx][ny] = '*'
                queue.append([nx, ny, 0])

print("KAKTUS")