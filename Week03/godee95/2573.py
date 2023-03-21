# 참고자료 https://youtu.be/45SoXzX26os

# 분류 : fail
# 56~59% 시간초과&메모리초과 발생!!

import sys
input = sys.stdin.readline
from collections import deque

sys.setrecursionlimit(10 ** 6)

R, C = map(int, input().rstrip().split())

iceberg = [list(map(int, input().split())) for _ in range(R)]

# 빙산의 갯수 카운트
melt = [[0 for _ in range(C)] for _ in range(R)] # sub =[[0]*C for _ in range(R)]

# 해당코드 실시간 반영으로 인해 값이 원하는대로 안나옴...흠....
# -> 접한 갯수를 계산하고 그 다음에 반영 값을 담을 sub 2차원 배열 필요!
# 배열의 첫번째 행과 열, 마지막 행과 열은 항상 0으로 채워지므로 탐색할 필요 없음!
# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c, visited):
    q = deque()
    q.append((r, c))
    
    while q:
        nr, nc = q.popleft()
        for idx in range(4):
            # 동서남분 방향 방문한 적 없고 빙산이면
            if visited[nr+dr[idx]][nc+dc[idx]] == 0 and iceberg[nr+dr[idx]][nc+dc[idx]] > 0:
                visited[nr+dr[idx]][nc+dc[idx]] = 1 # 방문처리
                q.append((nr+dr[idx], nc+dc[idx]))

# 1 ~ 900000 년(300*300) 전체 순회 반복작업
for year in range(1, 900000):
    # 녹는 빙산의 높이
    for r in range(1, R-1):
        for c in range(1, C-1):
            if iceberg[r][c] != 0:
                cnt = 0
                for idx in range(4):
                    # 배열 인덱스 범위 초과하지 않도록.
                    if iceberg[r+dr[idx]][c+dc[idx]] == 0:
                        cnt += 1
                melt[r][c] = cnt

    # 빙산 높이 낮추기
    for r in range(1, R-1):
        for c in range(1, C-1):
            if iceberg[r][c] > 0: # 이 경우 외에는 빙산 높이 낮추기 할 필요 없기 때문에!
                iceberg[r][c] = max(0, iceberg[r][c]- melt[r][c])

    # 빙산의 덩어리 갯수 카운트
    visited = [[0 for _ in range(C)] for _ in range(R)]

    cnt = 0
    for r in range(1, R-1):
        for c in range(1, C-1):
            if visited[r][c] == 0 and iceberg[r][c] > 0:
                cnt += 1
                if cnt > 1:
                    print(year)
                    exit()
                
                visited[r][c] = 1
                bfs(r,c,visited)

if cnt == 0:
    print(0)