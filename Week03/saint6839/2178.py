import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int,list(sys.stdin.readline().strip()))))


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

queue = deque()
visited = [[False for _ in range(M)] for _ in range(N)]
max = -sys.maxsize
def bfs(row, col, cost):
    global result, max

    queue.append([row, col, cost])
    visited[row][col] = True

    while queue:
        popped = queue.popleft()

        for i in range(4):
            nx = popped[0] + dx[i]
            ny = popped[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and board[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny, popped[2] + 1])

        if popped[0] == N-1 and popped[1] == M-1:
            if popped[2] > max:
                max = popped[2]


bfs(0, 0, 1)
print(max)