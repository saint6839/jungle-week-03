import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))


max = -sys.maxsize
min = sys.maxsize
def dfs(value, index):
    global max
    global min

    if not any(operators):
        if value > max:
            max = value
        if value < min:
            min =value
        return

    for i in range(len(operators)):
        if operators[i]:
            operators[i] -= 1
            if i == 0:
                dfs(value + numbers[index], index+1)
            elif i == 1:
                dfs(value - numbers[index], index+1)
            elif i == 2:
                dfs(value * numbers[index], index+1)
            else:
                dfs(int(value / numbers[index]), index+1)
            operators[i] += 1

dfs(numbers[0], 1)

print(max)
print(min)