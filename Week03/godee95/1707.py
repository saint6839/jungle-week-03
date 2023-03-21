#  -------------------- 런타임에러 OR 틀렸습니다 ----------------------
# 이문제 반례
# 1
# 4 3
# 2 3
# 3 4
# 4 2
# 1번 노드 들어가고 연결된게 아무것도 없으니 색칠하고 True로 반환. 
# 따라서 1번노드 탐색하고 그냥 True로 반환해버린다.

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9) # dfs 런타임에러 발생해서 추가한 코드!

# K = int(input().rstrip())

# result = []
# for _ in range(K):
#     V, E = map(int, input().rstrip().split(' '))

#     adj = [[] for _ in range(V+1)]
#     for _ in range(E):
#         a, b = map(int, input().rstrip().split(' '))
#         adj[a].append(b)
#         adj[b].append(a)

#     # 방문표시
#     # 방문표시와 색상표시를 함께 사용
#     visited = [False] * (V+1)
#     color = [0] * (V+1) # 방문한 노드는 1(빨간색) 또는 2(파란색)으로 표시함

#     # 탐색 함수
#     def DFS(node):
#         for next_node in adj[node]:
#             if visited[next_node] == False:
#                 visited[next_node] = True
#                 color[next_node] = 3 - color[node]  # 현재 노드와 다른 색상을 부여
#                 # 이미 방문한 노드를 다시 방문하게 되는 경우에도,
#                 # 해당 노드의 색상이 현재 노드와 같은지 체크해야 함!!
#                 if DFS(next_node) == False:
#                     return False
#             else:
#                 if color[next_node] == color[node]:  # 인접한 노드와 같은 색상을 가지면 False 반환
#                     return False
#         return True

#     visited[1] = True
#     # color[1] = 1  # 첫 번째 노드는 빨간색으로 시작
#     if DFS(1):
#         result.append("YES")
#         # print("YES")
#     else:
#         result.append("NO")
#         # print("NO")

# print(*result, sep='\n')


# -------------- 백준 통과 코드 ------------------

import sys
input = sys.stdin.readline
from collections import deque

K = int(input().rstrip())

result = []
for _ in range(K):
    V, E = map(int, input().rstrip().split(' '))

    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().rstrip().split(' '))
        adj[a].append(b)
        adj[b].append(a)

    # 탐색 함수
    def BFS(node):
        dq = deque()
        dq.append(node)
        color[node] = 1 # 처음 시작 노드는 빨간색으로 칠함

        while dq:
            cur_node = dq.popleft()
            for next_node in adj[cur_node]:
                if color[next_node] == 0: # 방문하지 않은 노드일 경우
                    color[next_node] = 3 - color[cur_node] # 현재 노드와 다른 색상 부여
                    dq.append(next_node)
                elif color[next_node] == color[cur_node]:
                    return False
        return True

    # 방문표시 및 컬러
    color = [0] * (V+1) # 방문한 노드는 1(빨간색) 또는 2(파란색)으로 표시함

    # 모든 노드를 돌면서 이분그래프 여부 판별
    # 연결된 노드든 연결되지 않은 노드든, 색이 같은 순간 break를 걸어 이분그래프 아니라고 표시하고 빠져나옴!!!
    bipartite = True
    for i in range(1, V+1):
        if color[i] == 0: # 방문하지 않은 노드일 경우
            if not BFS(i): # color 여부 확인
                bipartite = False
                break

    print("YES") if bipartite else print("NO")

    print(BFS(4))