# 분류 : fail

# 참고 자료 : https://technote-mezza.tistory.com/75
# -----------------------------------------------------------
# Floyd-Warshall 알고리즘
# 노드 쌍에 대해 최단 거리를 구하는 알고리즘

# 특별한 목적없이 모든 정점을 방문하는 완전탐색
# 현재 구슬보다 무겁거나 가벼운 구슬의 개수를 구하는 것이 목적

# 시작점에서 도달할 수 있는 모든 구슬을 구한다.
# 만약 도달할 수 있다면 나보다 무겁거나 가볍다는 의미

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [[0]*(N+1) for _ in range(N+1)]

half = N // 2 # 중간 구슬 갯수

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    arr[a][b] = 1 # a > b
    arr[b][a] = -1 # a < b

for i in range(1, N+1): # 거쳐가는 노드
    for j in range(1, N+1): # 출발 노드
        for k in range(1, N+1): # 도착노드
            # j->i, i->k
            # 잘 이해 안됨....
            # 출발구슬 -> 거쳐가는 구슬 -> 거쳐가는 구슬 -> 출발구슬
            # 출발구슬이 도착구슬과 직접적인 연결이 아니어도 위치가 지정되는 조건이 하나 더 성립
            if arr[k][i] != 0 and arr[j][i] == arr[i][k]:
                # print(f'j : {j}, k : {k}, i : {i}')
                arr[j][k] = arr[j][i] # 출발노드와 도착노드와의 관계 update

big = [0]*(N+1)
small = [0]*(N+1)

# i 구슬보다 큰 구슬의 갯수
# i 구슬보다 작은 구슬의 갯수
for i in range(1, N+1):
    for j in range(1, N+1):
        if arr[i][j] == 1:
            big[i] += 1
        if arr[i][j] == -1:
            small[i] += 1
# print(f'big : {big}')
# print(f'small : {small}')

ans = 0
for i in range(N+1):
    if big[i] > half:
        ans += 1
    if small[i] > half:
        ans += 1

print(ans)