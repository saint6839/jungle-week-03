import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().rstrip().split())

board = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

queue = deque()

for z in range(H):
    for y in range(N):
        for x in range(M):
            if board[z][y][x] == 1:
                queue.append([z, y, x])

dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, -1, 1]

while queue:
    pz, py, px = queue.popleft()
    for i in range(6):
        nz = pz + dz[i]
        ny = py + dy[i]
        nx = px + dx[i]
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and board[nz][ny][nx] == 0:
            board[nz][ny][nx] = board[pz][py][px] + 1
            queue.append([nz, ny, nx])

check = True
result = -sys.maxsize

for z in range(H):
    for y in range(N):
        for x in range(M):
            if board[z][y][x] == 0:
                check = False
            result = max(result, board[z][y][x])

if not check:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)



