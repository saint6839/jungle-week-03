# 분류 : accepted

# 5639 이진검색트리

# 공부 자료 : https://khsung0.tistory.com/28

# ---------------------------------------------
# 이진트리
# 노드 > 왼쪽 자식
# 노드 < 오른쪽 자식

# 전위순회
# 먼저 자기 자신을 처리
# 왼쪽 자식을 방문
# 오른쪽 자식을 방문

# 현재 원소보다 작은 원소들을 왼쪽 서브 트리
# 련재 원소보다 큰 원소들을 오른쪽 서브 트리
# 현재 노드

import sys
sys.setrecursionlimit(10**6)  # 재귀 호출의 최대 깊이를 10^6으로 설정

input = sys.stdin.readline

nums = []
while True:
    try:
        nums.append(int(input().rstrip()))
        pass
    except:
        break

# 이 작은 작업을 반복!
# left = 0
# right = len(nums) - 1

# for i in range(left+1, right+1):
#     if nums[left+1] < nums[i]:
#         mid = i
#         break
# right = mid
# left += 1

def post_order(left, right):
    # mid값이 탈출해야함!! mid가 right보다 커야 탈출하므로 right+1인듯!
    mid = right + 1 # post_order(left+1, mid-1) 탐색 끝난뒤, post_order(mid, right) 탈출할때 이 조건 필요!

    if left > right:
        return # 탐색 종료 조건 
    
    for i in range(left+1, right+1):
        if nums[left+1] < nums[i]:
            mid = i
            break

    post_order(left+1, mid-1) # 왼쪽 자식노드 # mid값이 i로 변하는 부분
    post_order(mid, right) # 오른쪽 자식노드 
    print(nums[left])


post_order(0, len(nums)-1)