import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline().rstrip())
inputs = sys.stdin.readline().rstrip()

in_or_out = [-1]
for i in range(len(inputs)):
    in_or_out.append(int(inputs[i]))

graph = [[] for _ in range(len(inputs)+1)]

for _ in range(2, len(inputs)+1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

result = 0
def dfs(start):
    global result
    isVisits[start] = True
    for i in graph[start]:
        if in_or_out[i] == 0 and not isVisits[i]:
            isVisits[i] = True
            dfs(i)
        elif in_or_out[i] == 1 and not isVisits[i]:
            isVisits[i] = True
            result += 1

for i in range(1, N+1):
    isVisits = [False for i in range(N+1)]
    if in_or_out[i]:
        dfs(i)

print(result)