import sys
sys.setrecursionlimit(10**5)

N, M = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


isVisits = [[False for _ in range(M)] for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and isVisits[nx][ny]:
            isVisits[nx][ny] = False
            if board[nx][ny]:
                dfs(nx, ny)
area = 0
while True:
    area += 1
    for x in range(N):
        for y in range(M):
            if board[x][y]:
                isVisits[x][y] = True
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and not isVisits[nx][ny]:
                        if not board[nx][ny]:
                            board[x][y] -= 1
                            if board[x][y] == 0:
                                break
    print(*board, sep='\n')
    check = 0
    for x in range(N):
        for y in range(M):
            if board[x][y] and isVisits[x][y]:
                dfs(x, y)
                check += 1
            elif not board[x][y] and isVisits[x][y]:
                isVisits[x][y] = False

    if check >= 2:
        print(area)
        break
    elif check == 0:
        print(0)
        break

