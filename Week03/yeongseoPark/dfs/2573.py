"""
0아닌건 미리 기록해둠
매 반복마다 0 아닌애들 마이너스 해줌
그리고 아무데서나 dfs함
dfs한 length가 0 아닌애들 길이보다 짧으면 두 덩어리 된거
"""
import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, sys.stdin.readline().split())

notZero = set()

# 행렬만들기, 0아닌것은 기록해줌
matrix = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if tmp[j] != 0:
            notZero.add((i,j))
    matrix.append(tmp)

# 동 서 남 북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# 해당 위치에서 주변 0 세기
def around_zero(row, col):
    cnt = 0

    for i in range(4):
        newR = row + dr[i]
        newC = col + dc[i]

        # 첫 마지막 행열은 항상 바다
        if 0 <= newR < n and 0 <= newC < m:
            if matrix[newR][newC] == 0:
                cnt += 1
    return cnt

# dfs하며 깊이만큼 cnt 더해줌
def dfs(row, col): # O(n)
    global cnt
    cnt += 1
    visited[row][col] = True

    for i in range(4):
        newR = row + dr[i]
        newC = col + dc[i]

        if 0 < newR < n-1 and 0 < newC < m-1 and not visited[newR][newC]:
            if matrix[newR][newC] != 0:
                dfs(newR, newC)


ans = 0
while True: 
    ans += 1

    # 전부 다 녹을때까지 덩어리 분리 X
    if len(notZero) == 0:
        print(0)
        break
    
    # 이거 같은 시간대에 미리 녹인쪽이 다른 쪽에 영향을 주면 안됨 - 일괄업데이트 필요
    update = []  # 넣고 빼는데 시간이 너무 드는데, 그렇다고 바로 업데이트하자니 이상하게 녹음
    for i in notZero: # zero 아닌것들 모두 녹여줌
        cnt = around_zero(i[0], i[1]) 
        newVal = matrix[i[0]][i[1]] - cnt
        if newVal <= 0: 
            update.append((i[0], i[1], 0))
        else:
            update.append((i[0], i[1], newVal))
    
    for i in update:
        if i[2] == 0: # 0된애들은 빼줌
            notZero.remove((i[0], i[1]))

        matrix[i[0]][i[1]] = i[2]
    
    # 0아닌것들 중 암거나 dfs해서, 0 아닌것들의 길이보다 짧으면 끝냄
    """
    visited 배열 말고, set에 (로우,컬럼) 저장하는 식으로 하면 시간초과 나고
    배열 쓰면 시간초과 안나는데, 둘다 O(1)아님??
    """
    visited = [[0] * m for _ in range(n)]
    for i in notZero:
        cnt = 0
        dfs(i[0], i[1])
        if cnt < len(notZero):
            print(ans)
            exit()
        break
    

     