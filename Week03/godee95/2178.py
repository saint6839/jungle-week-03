# 참고 자료 : https://youtu.be/ATs2_KiBV2E

# 최소 칸 수로 이동

import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().rstrip().split())

# 미로
arr = [list(map(int, input().strip())) for _ in range(R)]

# 방문표시
visited = [[0]*C for _ in range(R)]

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def BFS(r,c, er, ec):
    q = deque()
    q.append((r,c))
    visited[r][c] = 1 # 방문 표시

    while q:
        cur_r, cur_c = q.popleft()
        # 종료
        if (cur_r, cur_c) == (er, ec):
            return visited[er][ec]

        for i in range(4):
            nr, nc = cur_r+dr[i], cur_c+dc[i]
            # 범위 내 이고 다음 좌표가 길(1)이고 방문을 안한 곳이라면,
            if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = visited[cur_r][cur_c] + 1

answer = BFS(0, 0, R-1, C-1)
print(answer)