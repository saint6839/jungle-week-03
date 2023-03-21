"""
3차원 그래프

매 사이클마다 위, 아래, 동/서/남/북 인접한 익은 토마토의 영향을 받아 익게됨
주변에 하나만 있으면 익는듯 

[ 
    [
        [
        
        ]
    ],

    [
        [
        
        ]
    ]
    ...
]
"""
import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split()) # 가로 , 세로 , 높이 

que = deque([])

# 상자 생성
box = []
for i in range(h):
    pan = []
    for j in range(n):
        tmp = list(map(int, sys.stdin.readline().split()))
        for k in range(m):
            if tmp[k] == 1:
                que.append((i, j, k))  # (height, row ,col) -- bfs할 큐에 익은 토마토들 넣어줌 
        pan.append(tmp)
    box.append(pan)

# 동 서 남 북 위 아래
dr = [0, 0, 1, -1, 0, 0]
dc = [1, -1, 0, 0, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

while que:
    hei, r, c = que.popleft()

    for i in range(6):
        newH = hei + dh[i]
        newR = r + dr[i]
        newC = c + dc[i]
        if 0 <= newH < h and 0 <= newR < n and 0 <= newC < m and box[newH][newR][newC] == 0: 
            que.append((newH, newR, newC))
            box[newH][newR][newC] = box[hei][r][c] + 1 
        # 익은 토마토에서 시작해서 1씩 더해가며 bfs로 0들을 탐색해나감
        # 전날 미리 1을 더해주기 때문에 -1을 해준 값이 답이다

ans = 0
for i in box:
    for j in i:
        for k in j:
            if k == 0: # 모든 탐색을 마쳤는데도 0이 있다면 익힐 수 없는 토마토인것
                print(-1)
                exit()
        ans = max(ans, max(j))

print(ans - 1)















# def rot(height, row, col):

#     for i in range(6):
#         newR = row + dr[i]
#         newC = col + dc[i]
#         newH = height + dh[i]
    
#         if 0 <= newR < n and 0 <= newC < m and 0 <= newH < h and box[newH][newR][newC] == 0:
#             willRot.append((newH, newR, newC))

# while True:
#     willRot = [] # 한 사이클에서 익을 애들
#     for i in rotten:
#         rot(i[0], i[1], i[2])
    
#     # 익히고, 익은 토마토에 추가
#     for i in willRot:
#         box[i[0]][i[1]][i[2]] = 1
#         rotten.add(i[0], i[1], i[2]) 
    
#     visited = [[[0] * m for _ in range(n)] for _ in range(h)]

#     break # 임시로

# from collections import deque
# def bfs(height, row, col):
#     global visited

#     deq = deque()
#     deq.append((height, row, col))
#     visited[height][row][col] = True

#     for i in range(6):
#         newR = row + dr[i]
#         newC = col + dc[i]
#         newH = height + dh[i]
    
#         if 0 <= newR < n and 0 <= newC < m and 0 <= newH < h