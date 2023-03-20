import sys

input = sys.stdin.readline

r, c= map(int, input().split())

graph = []
for _ in range(r):
    graph.append(list(input().strip()))

alphas = [0] * 26
visited = [[0] * c for _ in range(r)]

# 동 서 남 북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

ans = 0
real_visited = [[0] * c for _ in range(r)]

def dfs(row, col, cnt):
    global ans

    if cnt > ans:
        ans = cnt

    visited[row][col] = 1
    alphas[ord(graph[row][col]) - ord('A')] = True

    for i in range(4):
        newR = row + dr[i]
        newC = col + dc[i]

        if 0 <= newR < r and 0 <= newC < c and not alphas[ord(graph[newR][newC]) - ord('A')] and not visited[newR][newC]:
            dfs(newR, newC, cnt + 1)

    # dfs로 전체 다 탐색하는게 아니라, 경우의 수에 대해 가지치기를 해야되기 때문에
    # 해당 함수가 끝나면 방문배열과, 방문 알파벳을 배열에서 빼줘야한다
    alphas[ord(graph[row][col]) - ord('A')] = False
    visited[row][col] = 0    

dfs(0, 0, 1)
print(ans)



