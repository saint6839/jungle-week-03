"""
무방향 그래프, 연결 요소의 개수 구하기
정점 최대 1000, 
간선최대는 모든 정점쌍 사이가 간선으로 연결된 경우: n개가 n-1개와 연결, 양방향 간선이므로 2로 나눔 

connected componenet : 
어떤 두 정점들 사이이든 중간에 path가 있는 서브그래프, 
서로 연결되어 있는 여러개의 고립된 부분 그래프 각각을 의미

1 ~ n이니까
set에 넣고
1에서 bfs해서 탐색된것들 set에서 다 뺌
set에 남은것 아무거나 pop으로 꺼내서 bfs 
~ set없어질때까지 반복, 횟수 리턴 
"""
from collections import deque
import sys, random

input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}
for i in range(1, n+1):
    dic[i] = []

for _ in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

remainders = set([i for i in range(1, n+1)])

def bfs(start):
    visited = [0] * (n+1)

    que = deque()
    que.append(start)
    visited[start] = True
    remainders.remove(start) 

    while que:
        cur = que.pop()
        
        for i in dic[cur]:
            if not visited[i]:
                que.appendleft(i)
                remainders.remove(i) 
                visited[i] = True

# 이미 컴포넌트에 넣은 요소들 삭제에 O(1)만 사용하고 싶어서 set 사용
# 근데 set에서 랜덤요소를 꺼내려면 이렇게 list로 변환 후(인덱싱가능하게), 꺼내줘야 돼서
# list변환시의 시간복잡도 O(n)이 듬
# -> 그냥 for문으로 아무거나 꺼내면 됨
ans = 0
while remainders:
    ans += 1
    # sth = random.sample(list(remainders), 1)[0]
    for i in remainders:
        sth = i
        break

    bfs(sth)

print(ans)



