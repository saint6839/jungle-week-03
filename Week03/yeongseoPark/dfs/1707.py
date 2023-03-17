"""
이분 그래프 : 정점을 2그룹으로 나눌 수 있는데, 같은 그룹의 정점끼리는 간선으로 이어지지 않음 
간선 없이 정점만 있어도 이분 그래프
-> 임의로 2그룹으로 나눴는데, 각 그룹안의 정점끼리 이어지지 않기만 하면 됨

a 집합
b 집합
아무데서나 dfs함
시작은 a집합 
연결되는 정점은 b집합
여기서 연결되는 정점은 또 a집합.. 
근데 a 집합의 정점에서 탐색해서 간 곳이 또 a집합이면 이분그래프 아닌 것 
근데 a집합에서 이미 방문한(집합에 넣은곳)에 또 갈수가 없네

dfs로 접근되지 않은 모든 정점들에 대해서 다해줘야 함, 
왜냐면 그래프가 아예 두개의 부분그래프로 나뉘는데, 하나는 이분이고 하나는 아닐 수 있기때문
"""
# 왜 18%에서 틀리는지 모르겠음 반례 찾기 실패 
# import sys

# sys.setrecursionlimit(10 ** 5)

# input = sys.stdin.readline

# k = int(input()) # 테스트 케이스의 개수 

# """
# cases = 
# [
#     [ 
#         정점 개수,
#         {정점 1 : [연결1 , 연결 2, ...]}
#     ], 
#     [ 
#         정점 개수,
#         {정점 1 : [연결1 , 연결 2, ...]}
#     ],
# ....
# ]
# """
# cases = []
# for i in range(k):
#     v, e = map(int, input().split()) 
#     per_case = [v] # 일단 정점 개수 넣음
#     dic = {i:[] for i in range(1, v+1)}
#     for _ in range(e):
#         a, b = map(int, input().split())
#         dic[a].append(b)
#         dic[b].append(a)
    
#     per_case.append(dic)

#     cases.append(per_case)

# def dfs(cur, team):
#     visited[cur] = True
#     RB[cur] = team
#     next = 1 if team == 2 else 2

#     for i in relation[cur]:
#         if RB[i] == RB[cur]:  # 인접 정점인데 나랑 팀이 같음
#             return False

#     for i in relation[cur]: # 인접 정점들의 집합을 결정
#         RB[i] = next
        
#     for i in relation[cur]:
#         if not visited[i]:
#             return dfs(i , next)

# # 최종 결과 배열
# ans = []  

# for case in cases:
#     node_count = case[0]
#     relation   = case[1]

#     visited = [0] * (node_count + 1)
#     RB = [0] * (node_count + 1) # 어느 그룹에 속하는지

#     error = False
#     for i in range(1, node_count + 1):
#         if not visited[i]:
#             if RB[i] != 0: # 팀이 이미 정해진경우는 그 팀으로 탐색해야함
#                 if dfs(i, RB[i]) == False:
#                     ans.append("NO")
#                     error = True
#                     break
#                 else:
#                     pass

#             else:
#                 if dfs(i, 1) == False:
#                     ans.append("NO")
#                     error = True
#                     break
#                 else:
#                     pass
    
#     if error:
#         continue
#     ans.append("YES")
    
# for i in ans:
#     print(i)      

"""
답봄 
"""
import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

k = int(input())

def dfs(start, group):
    visited[start] = group # 정점의 그룹 설정(-1, 1)

    for i in graph[start]:
        if not visited[i]:
            a = dfs(i, -group)
            if not a: # dfs의 결과가 false
                return False
        
        elif visited[i] == visited[start]:
            return False
    
    return True

for _ in range(k):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v+1)]

    visited = [False] * (v+1)

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1, v+1):
        if not visited[i]:
            result = dfs(i, 1) 
            if not result:
                break
    
    print("YES" if result else "NO")
