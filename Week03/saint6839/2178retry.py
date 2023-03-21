import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

board = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[False for _ in range(M)] for _ in range(N)]
def bfs(x, y):

    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    while queue:
        px, py = queue.popleft()

        if px == N-1 and py == M-1:
            print(board[px][py])
            break

        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                board[nx][ny] = board[px][py] + 1
                queue.append([nx, ny])

bfs(0, 0)
