import heapq
import sys

N = int(sys.stdin.readline())

board = [list(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(N)]

visited = [[False for _ in range(N)] for _ in range(N)]


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    priority_queue = []
    visited[x][y] = True
    heapq.heappush(priority_queue, (0,x,y))

    while priority_queue:
        pcost, px, py = heapq.heappop(priority_queue)
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    if board[nx][ny] == 1:
                        heapq.heappush(priority_queue, (pcost, nx, ny))
                    else:
                        heapq.heappush(priority_queue, (pcost + 1, nx, ny))

        if px == N-1 and py == N-1:
            print(pcost)
bfs(0, 0)
