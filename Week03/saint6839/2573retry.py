import sys
sys.setrecursionlimit(10**4)
N, M = map(int, sys.stdin.readline().split())

boards = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[False for _ in range(M)] for _ in range(N)]

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M  and visited[nx][ny] and boards[nx][ny]:
            visited[nx][ny] = False
            dfs(nx, ny)

year = 0
while True:
    year += 1
    for i in range(N):
        for j in range(M):
            if boards[i][j]:
                visited[i][j] = True
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        if boards[nx][ny] == 0:
                            boards[i][j] -= 1
                            if boards[i][j] == 0:
                                break
    area = 0

    for i in range(N):
        for j in range(M):
            if boards[i][j] == 0:
                visited[i][j] = False
            if visited[i][j]:
                area += 1
                visited[i][j] = False
                dfs(i, j)

    if area >= 2:
        print(year)
        break
    elif area == 0:
        print(0)
        break