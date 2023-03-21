import heapq
import sys

N = int(sys.stdin.readline())
board = [list(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

queue = []
def bfs(cost, x, y):
    visited[x][y] = True
    heapq.heappush(queue, [cost, x, y])

    while queue:
        popped = heapq.heappop(queue)
        p_cost = popped[0]
        px = popped[1]
        py = popped[2]

        if px == N-1 and py == N-1:
            print(p_cost)
            break

        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] == 1:
                    heapq.heappush(queue, [p_cost, nx, ny])
                else:
                    heapq.heappush(queue, [p_cost + 1, nx, ny])

bfs(0, 0, 0)