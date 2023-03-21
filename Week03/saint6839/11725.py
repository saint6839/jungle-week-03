import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())

isVisits = [False for _ in range(N+1)]

connections = [[] for _ in range(N+1)]


for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    connections[a].append(b)
    connections[b].append(a)

results = dict()
def dfs(start):
    isVisits[start] = True

    for i in connections[start]:
        if not isVisits[i]:
            dfs(i)
            results[i] = start

dfs(1)
for i in range(2, N+1):
    print(results[i])