import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

time = [0] * (n+1)
in_degree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
cnt = [[] for _ in range(n+1)]

for _ in range(m):
    # a -> b, 걸리는 시간 c
    a, b ,c = map(int, input().split())
    graph[a].append((c,b)) 
    in_degree[b] += 1

# 출발 -> 도착 
src, dst = map(int, input().split())

q = deque()
q.append(src)

# 기본적인 위상정렬에, v까지의 비용중 최고비용을 time[v]에 저장하는 것과, v로 향하는 최고비용의 경로의 전 정점을 cnt[v]에 저장하는 것을 더한 코드
while q:
    now = q.pop()

    for cost, next in graph[now]:
        in_degree[next] -= 1
        # now를 거쳐서 가는 비용이 더 크다면 걔로 time을 갱신
        if time[next] < time[now] + cost:
            time[next] = time[now] + cost
            # next에 도착하기 직전에 거쳐온 노드를 기록한 리스트를 비우고
            # 달려야 하는 도로를 현재위치 now하나로 갱신
            cnt[next] = [now]
        
        # 도착지까지 같은 시간이 걸리면서 가는 경로가 여러개, 따라서 now를 추가
        # 1->2->5 / 1->2->3->5 같은 경우 
        elif time[next] == time[now] + cost:
            cnt[next].append(now)
        
        if in_degree[next] == 0:
            q.appendleft(next)

# 지나온 경로 역추적, 이미 지나온 경로들은 큐에 넣지 않아서 시간초과 방지
q = deque([dst])
route = set()
while q:
    now = q.pop()
    for x in cnt[now]: # cnt[now]에 now로 향하는 최고비용 경로들의 전 정점을 기록했으므로, x가 전 정점인 꼴
        if (now, x) not in route:
            route.add((now, x))
            q.appendleft(x)

print(time[dst])
print(len(route))
            