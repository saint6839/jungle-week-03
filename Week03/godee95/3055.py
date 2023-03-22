# 분류 : fail

# 반례
# 5 5
# D...*
# ..XXX
# .....
# .....
# .S...
# answer : 5

import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
grid = [input().rstrip() for _ in range(R)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs():
    hedgehog = deque()
    water = deque()
    time = [[-1]*C for _ in range(R)]
    
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'S':
                hedgehog.append((r, c))
                time[r][c] = 0
            elif grid[r][c] == '*':
                water.append((r, c))
            elif grid[r][c] == 'D':
                end_r, end_c = r, c
                
    while hedgehog:
        for _ in range(len(water)):
            r, c = water.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < R and 0 <= nc < C and (grid[nr][nc] == '.' or grid[nr][nc] == 'S'):
                    # 특정 인덱스에 있는 요소를 변뎡라는 코드
                    grid[nr] = grid[nr][:nc] + '*' + grid[nr][nc+1:]
                    # grid[nr][nc] = '*' # 문자열이기 때문에 불가능.ㅠ
                    water.append((nr, nc))
        
        for _ in range(len(hedgehog)):
            r, c = hedgehog.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '*' and grid[nr][nc] != 'X' and time[nr][nc] == -1:
                    time[nr][nc] = time[r][c] + 1
                    hedgehog.append((nr, nc))
                    
                    if nr == end_r and nc == end_c:
                        return time[nr][nc]
                        
    return "KAKTUS"

print(bfs())
