# 분류 : accepted

# 3차원 BFS
# 6방향 : 위, 아래, 왼쪽, 오른쪽, 앞, 뒤

import sys
input = sys.stdin.readline
from collections import deque

# 입력받고
M, N, H = map(int, input().rstrip().split())
tomato = [[list(map(int, input().rstrip().split())) for _ in range(N)] for _ in range(H)] # 3차원

# 솔루션
def bfs():
    # 생성
    q = deque()
    visited = [[[0]*M for _ in range(N)] for _ in range(H)]

    # q에 초기 데이터들 삽입, 안익은 토마토 카운트
    cnt = 0
    # 전체 순회, 익은 토마토 위치 q에 저장, 안 익은 토마토 갯수 카운트
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if tomato[h][r][c] == 1: # 익은 토마토
                    q.append((h, r, c))
                    visited[h][r][c] = 1
                elif tomato[h][r][c] == 0: # 안 익은 토마토
                    cnt += 1

    while q:
        cur_h, cur_r, cur_c = q.popleft()
        # 6방향, 북동남서위아래
        for dh, dr, dc in ((0,-1,0), (0,0,1), (0,1,0), (0,0,-1), (-1,0,0),(1,0,0)):
            next_h, next_r, next_c = cur_h+dh, cur_r+dr, cur_c+dc
            # 범위내에 있고 방문한적 없고 악익은 토마토라면,
            if  0<=next_h<H and 0<=next_r<N and 0<=next_c<M and not visited[next_h][next_r][next_c] and tomato[next_h][next_r][next_c] == 0:
                q.append((next_h, next_r, next_c))
                visited[next_h][next_r][next_c] = visited[cur_h][cur_r][cur_c] + 1
                cnt -= 1 # 안 익은 토마토를 방문하게 되면 익게 되므로 카운트 줄여주기

    # 다 방문하고 나서고 cnt가 0이 아니면 return -1
    if cnt == 0:
        return (visited[cur_h][cur_r][cur_c] - 1)
    else:
        return -1

# 출력
ans = bfs()
print(ans)