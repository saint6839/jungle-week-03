# """
# . : 비어잇음
# * : 물 
# X : 돌
# D : 굴
# S : 고슴도치

# 동서남북 이동
# 매분마다 물은 비어있는 칸으로 확장

# 돌 통과 불가 / 물 통과 불가 / 다음 시간에 물이 차는 곳으로 이동 불가

# 고슴도치 -> 굴
# 의 최소시간

# 50 * 50 , 시간제한 1초
# """
# import sys
# from collections import deque

# input = sys.stdin.readline

# r, c = map(int, input().split())

# map = []
# for i in range(r):
#     tmp = list(input().strip())
#     for j in range(len(tmp)):
#         if tmp[j] == 'S':
#             initial = (i, j, 0) #  끝은 시간값
#     map.append(tmp)             


# # 돌, 물 못가고 / 다음 시간에 물 차는곳 못감
# # 물을 그냥 먼저 채우고(fill 함수)
# # 거기다가 bfs

# # 동 서 남 북
# dr = [0, 0, 1, -1]
# dc = [1, -1, 0, 0]

# # 물 될애들 기록해뒀다가 일괄기록
# def fill():
#     change = []
#     for i in range(r):
#         for j in range(c):
#             if map[i][j] == '*':
#                 for k in range(4):
#                     RR = i + dr[k]
#                     CC = j + dc[k]
#                     if 0 <= RR < r and 0 <= CC < c and map[RR][CC] != 'X' and map[RR][CC] != 'D':
#                         change.append((RR,CC))
    
#     for i in change:
#         map[i[0]][i[1]] = '*'

# deq = deque()
# deq.append(initial)

# while deq:
#     row, col, cur = deq.pop()

#     # 물 채우기
#     fill()

#     for k in range(4):
#         newR = row + dr[k]
#         newC = col + dc[k]
    
#         if 0 <= newR < r and 0 <= newC < c and map[newR][newC] != 'X' and map[newR][newC] != '*':
#             if map[newR][newC] == 'D':
#                 print(cur + 1)
#                 exit()
#             else:
#                 deq.append((newR, newC, cur+1))
#                 map[newR][newC] = cur + 1

# print("KAKTUS")

"""
매번 BFS마다 물 채우고, 이동시키려니까 꼬임 

물따로, 도치 따로 bfs해서 
굴 주변에 도치가 하나라도 먼저 도착했는지 체크
"""
import sys, copy
from heapq import heappush, heappop

input = sys.stdin.readline

r, c = map(int, input().split())

wat = [] 
map = []
for i in range(r):
    tmp = list(input().strip())
    for j in range(len(tmp)):
        if tmp[j] == 'S':
            initial = (0, i, j) # 맨 앞이 가중치 끝은 시간값
        if tmp[j] == '*':
            wat.append((0, i, j))
        if tmp[j] == 'D':
            cav = (i, j)
    map.append(tmp)  

map_water = copy.deepcopy(map)           

# 동 서 남 북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

visited = [[0] * c for _ in range(r)]

heap = []
heappush(heap, initial)
map[initial[1]][initial[2]] = 0
visited[initial[1]][initial[2]] = True

while heap:
    cost, row, col = heappop(heap)
    
    map[row][col] = cost

    for k in range(4):
        newR = row + dr[k]
        newC = col + dc[k]
    
        if 0 <= newR < r and 0 <= newC < c and map[newR][newC] != 'D' and  map[newR][newC] != 'X' and map[newR][newC] != '*' and not visited[newR][newC]:
            visited[newR][newC] = True 
            heappush(heap, (cost + 1, newR, newC))

if wat == []:
    ans = sys.maxsize
    for i in range(4):
        newR = cav[0] + dr[i]
        newC = cav[1] + dc[i]

        if 0 <= newR < r and 0 <= newC < c:
            cat = map[newR][newC]
        
    if type(cat) == int:
        ans = min(ans, cat + 1)
    
    if ans == sys.maxsize:
        print("KAKTUS")
    else:
        print(ans)
    exit()


visited = [[0] * c for _ in range(r)]
heap = []
for i in wat:
    heappush(heap, i)
    map_water[i[1]][i[2]] = 0
    visited[i[1]][i[2]] = True
while heap:
    cost, row, col = heappop(heap)

    map_water[row][col] = cost

    for k in range(4):
        newR = row + dr[k]
        newC = col + dc[k]
    
        if 0 <= newR < r and 0 <= newC < c and map_water[newR][newC] != 'X' and not visited[newR][newC] and map_water[newR][newC] != 'D':
            visited[newR][newC] = True 
            heappush(heap,(cost+1, newR, newC))

for i in range(r):
    for j in range(c):
        if type(map_water[i][j]) != int:
            map_water[i][j] = sys.maxsize
        if type(map[i][j]) != int:
            map[i][j] = sys.maxsize

ans = sys.maxsize
for i in range(4):
    newR = cav[0] + dr[i]
    newC = cav[1] + dc[i]

    if 0 <= newR < r and 0 <= newC < c:
        cat   = map[newR][newC]
        water = map_water[newR][newC]

        if cat < water:
            ans = min(ans, cat + 1)

if ans == sys.maxsize:
    print("KAKTUS")
else:
    print(ans)



# min_cat = sys.maxsize
# for i in range(4):
#     newR = cav[0] + dr[i]
#     newC = cav[1] + dc[i]

#     cat   = map[newR][newC]
#     water = map_water[newR][newC]

#     ans = sys.maxsize

#     if type(cat) == int and type(water) == int:
#         if cat < water:
#             ans = min(ans, cat + 1)

#     elif type(cat) != int and type(water) == int:
#         continue

#     elif type(cat) == int and type(water) == int:
#         ans = min(ans, cat + 1)
    
#     elif type(cat) != int and type(water) != int:
#         print("KAKTUS")
#         exit()
    
# if ans == sys.maxsize:
#     print("KAKTUS")
# else:
#     print(ans)




        