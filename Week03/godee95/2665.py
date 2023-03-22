# 분류 : accepted
# 길일때 그 방향으로만 가도록 우선수위 큐 이용!!!

# 백준 미로 만들기
import sys
input = sys.stdin.readline
from collections import deque

n = int(input().rstrip())

maze = [list(map(int, list(input().rstrip()))) for _ in range(n)]

# visited[a][b] = c, (a,b)좌표까지 오는데 1을 0으로 바꾼 갯수는 c입니다.
visited = [[-1]*n for _ in range(n)]

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def BFS():
    # 생성
    q = deque()
    q.append((0,0))
    visited[0][0] = 0 # 시작점 방문 표시

    while q:
        cur_r, cur_c = q.popleft()

        for i in range(4):
            nr, nc = cur_r + dr[i], cur_c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == -1:
                # 벽이라면, 뿌수고 이동
                if maze[nr][nc] == 0:
                    visited[nr][nc] = visited[cur_r][cur_c] + 1
                    q.append((nr, nc))
                else:
                    # 길이라면 그 길로 이동!!
                    visited[nr][nc] = visited[cur_r][cur_c]
                    q.appendleft((nr, nc)) # 우선순위를 높이기 위해 appendleft 사용

BFS()
print(visited[n-1][n-1])