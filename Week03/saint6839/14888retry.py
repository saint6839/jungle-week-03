import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))


max = -sys.maxsize
min = sys.maxsize

visited = [False for _ in range(N)]
def dfs(index, sum):
    global max
    global min

    if not any(operators):
        if max < sum:
            max = sum
        if min > sum:
            min = sum
        return

    for i in range(len(operators)):
        if operators[i]:
            operators[i] -= 1
            if i == 0:
                dfs(index + 1, sum + numbers[index])
            elif i == 1:
                dfs(index + 1, sum - numbers[index])
            elif i == 2:
                dfs(index + 1, sum * numbers[index])
            elif i == 3:
                dfs(index + 1, int(sum / numbers[index]))
            operators[i] += 1

dfs(1, numbers[0])

print(max)
print(min)

