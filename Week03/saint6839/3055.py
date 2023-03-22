import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())

boards = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
queue = deque()

for i in range(R):
    for j in range(C):
        if boards[i][j] == 'S':
            queue.append([i, j, 0])

for i in range(R):
    for j in range(C):
        if boards[i][j] == '*':
            queue.append([i, j, 0])

dx = [-1, 0, 1 ,0]
dy = [0, -1, 0, 1]
def bfs():
    while queue:
        px, py, pcost = queue.popleft()

        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if (boards[nx][ny] == '.' or boards[nx][ny] == 'D') and boards[px][py] == 'S':
                    if boards[nx][ny] == 'D':
                        print(pcost + 1)
                        print(*boards, sep='\n')
                        exit(0)
                    boards[nx][ny] = 'S'
                    queue.append([nx, ny, pcost + 1])
                elif (boards[nx][ny] == '.' or boards[nx][ny] == 'S') and boards[px][py] == '*':
                    boards[nx][ny] = '*'
                    queue.append([nx, ny, 0])
bfs()
print("KAKTUS")
