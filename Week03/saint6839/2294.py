
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())

coins = set()
for _ in range(n):
    coins.add(int(sys.stdin.readline()))
checks = [0 for _ in  range(k + 1)]

queue = deque()
for coin in coins:
    if coin > k:
        continue
    queue.append([coin, 1])
    checks[coin] = 1

flag = True
def bfs():
    global flag

    while queue:
        value, count = queue.popleft()
        if value == k:
            print(count)
            flag = False
            break

        for coin in coins:
            if value + coin > k:
                continue
            if not checks[value + coin]:
                checks[value + coin] = 1
                queue.append([value + coin, count + 1])
bfs()

if flag:
    print(-1)