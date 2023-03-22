# 분류 : fail

# 참고 자료 : https://velog.io/@grace0st/%EB%8F%99%EC%A0%842-%EB%B0%B1%EC%A4%80-2294%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC

# n, k가 주어진다.
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
coins = []
for _ in range(n):
    coin = int(input().rstrip())
    coins.append(coin)

# 1 ≤ k ≤ 10,000
# 최소갯수를 구하는 것이기 때문에 dp에 최댓값을 넣어준다.
dp = [0]+[10001]*(k)
 
for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])