import sys

N = int(sys.stdin.readline())
pair = int(sys.stdin.readline())

isConnected = [[False for _ in range(N+1)] for _ in range(N+1)]
isVisits = [False for _ in range(N+1)]

for _ in range(pair):
    a, b = map(int, sys.stdin.readline().split())
    isConnected[a][b] = True
    isConnected[b][a] = True

result = 0
def dfs(start):
    global result
    isVisits[start] = True

    for i in range(1, N+1):
        if not isVisits[i] and (isConnected[start][i] or isConnected[i][start]):
            isVisits[i] = True
            result += 1
            dfs(i)

dfs(1)
print(result)