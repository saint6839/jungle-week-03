# 분류 : accepted

import sys
input = sys.stdin.readline

N = int(input().rstrip())
numbers = list(map(int, input().strip().split()))
plus, minus, mul, div = map(int, input().rstrip().split())

min_val = float("inf")
max_val = float("-inf")

# 여러 연산을 재귀적으로 하기 위해서는 cur_idx와 cur_result를 파라미터로 두는 것이 중요!!
# 현재 cur_result + numbers[cur_idx] 이런 식으로 재귀를 돌려야 하므로 idx접근할 수 있는 코드로 짜는게 중요함.
def dfs_operator(plus, minus, mul, div, cur_result, cur_idx):
    global min_val, max_val

    if cur_idx == N:
        min_val = min(min_val, cur_result)
        max_val = max(max_val, cur_result)
        return
    else:
        if plus:
            dfs_operator(plus-1, minus, mul, div, cur_result+numbers[cur_idx], cur_idx+1)
        if minus:
            dfs_operator(plus, minus-1, mul, div, cur_result-numbers[cur_idx], cur_idx+1)
        if mul:
            dfs_operator(plus, minus, mul-1, div, cur_result*numbers[cur_idx], cur_idx+1)
        if div:
            dfs_operator(plus, minus, mul, div-1, int(cur_result/numbers[cur_idx]), cur_idx+1)

# cur_result, cur_idx값 설정 중요!
dfs_operator(plus, minus, mul, div, numbers[0], 1)

print(min_val)
print(max_val)