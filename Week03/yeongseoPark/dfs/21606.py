# """
# 실내 시작 ~ 실내 도착
# 중간에 실내가 있으면 안됨
# -> 의 경로가 몇개인지

# 정점의 개수가 2 * 10^5 이므로 recursionlimit 풀고 dfs가능
# dfs면 O(N)인가?

# 주어진 문자열 for문 돌면서
# 1. 실내면 dfs 시작
# 2. 또 실내를 만나면 끝냄 
# 3. 어차피 실내 또 만나면 끝나니까 굳이 set에 넣어서 고유성 유지 필요X인듯
# 4. 그냥 실내를 또 만나면 결과 + 1 하고 리턴시켜주면 됨 
# """



"""
60점 
"""
# import sys

# input = sys.stdin.readline

# n = int(input())

# # 실내 실외
# given = input().strip()
# path = [-1]
# for i in range(1, n+1):
#     path.append(int(given[i-1]))

# graph = [[] for _ in range(n+1)]

# # 간선 입력받음
# for _ in range(n-1):
#     a, b= map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# res = 0 

# def dfs(start): 
#     global res

#     visited[start] = True

#     for i in graph[start]:
#         if not visited[i]:
#             if path[i] == 1:
#                 res += 1
#                 continue
#             else: 
#                 dfs(i)

# for i in range(1, n+1): O(N^2) 
#     visited = [0] * (n+1)
    
#     if path[i] == 1:
#         dfs(i)  # O(N)?

# print(res)
             
"""
실내 ~ 실내
실외를 컴포넌트로 생각해서, 실외에 인접한 실내들을 dfs로 세기
예를들어 실외 하나에 실내가 5개 인접했으면, 5의 실내들은 자기를 제외한 4개 선택가능
따라서 5 * 4 최종 결과에 더해줌
실내 ~ 실내로 실외를 거치지 않고 가는 경우도 * 2해서 더해주면 됨
이미 방문한 곳은 또 갈 필요 없음 

모든 노드 순회에 O(N),
dfs가 있으나 방문한 곳은 또 가지 않기 때문에 최종 O(N)
"""
import sys
sys.setrecursionlimit(10 ** 9)

n = int(sys.stdin.readline())

# 실내 실외
path = sys.stdin.readline().strip()

# 인접 그래프
graph = [0]
for _ in range(n):
    graph.append([])

res = 0 # 최종 결과 

# 간선 입력받음
for _ in range(n-1):
    a, b= map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

    # 실내 - 실내면 바로 += 2 해줌
    if path[a-1] == "1" and path[b-1] == "1":
        res += 2

def dfs(start, cnt):
    visited[start] = True

    for i in graph[start]:
        if path[i - 1] == "0" and not visited[i]: # 실외로 가면
            cnt = dfs(i, cnt)
        elif path[i-1] == "1": # 실내로 가면
            cnt += 1
    return cnt

visited = [False] * (n+1)

for i in range(1, n+1):
    if not visited[i] and path[i-1] == "0": # 실외만 dfs
        # 어차피 "실내"로는 가지도 않으니까 visited배열은 실외만을 체크하기 위한 것
        # 실외에 대한 방문을 기록해주지 않으면 갔던 곳을 또가게 되고 그만큼 dfs재귀호출을 더하게됨
        # 그래서 스택프레임(지역변수,매개변수, 복귀주소)이 쌓여서? 메모리 초과가 난게 아닐까...
        # 호출이 깊어질 수 있게 recursion limit 은 열어줬지만, 스택 
        cnt = dfs(i, 0)
        res += cnt * (cnt - 1)

print(res)        
   

