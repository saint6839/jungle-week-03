# 전위 순회(루트 -> 왼쪽 -> 오른쪽) 을 후위순회(왼쪽 -> 오른쪽 -> 루트) 로

# 트리 클래스를 만들고
# 전위 순회한 결과를 height별로 나눠서 넣어줘야 함(height가 다르면 트리 자체가 달라짐)
# ㄴ 이럴 필요없이 그냥 넣어줘도 원래 트리 나올듯?
# 그리고 이거를 후위순회

# 노드의 수는 10000개 이하,
# 트리에 넣는데 O(n log n)
# 순회하는데 O(N)

class Node:
    def __init__(self, value, left, right):
        self.val = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root):
        self.root = root

    def add(self, root, added_val):
        if added_val == root.val:
            return False

        if root.val < added_val:
            if not root.right:
                root.right = Node(added_val, None, None)
            else:
                self.add(root.right, added_val)
        
        else:
            if not root.left:
                root.left = Node(added_val, None, None)
            else:
                self.add(root.left, added_val)

        return True

from collections import deque
import sys
# 파이썬 기본 재귀 깊이 1000을 풀어줌 - post함수의 깊이 최대 10000(한쪽으로 계속 이어졌을때
# 실험해보니까 한 8000정도 열어주면 recursionError 나지 않음
sys.setrecursionlimit(10 ** 5) # 10만, 10^6으로 두면 메모리 초과 발생

input = sys.stdin.readline

arr = deque()

while True:
    tmp = input().strip()

    if tmp == '':
        break

    arr.append(int(tmp))

root = Node(deque.popleft(arr), None, None)
bst = Tree(root)

while arr:
    tmp = deque.popleft(arr)

    bst.add(root, tmp)

# recursion error
def post(root):
    if root.left:
        post(root.left)
    if root.right:
        post(root.right)
    print(root.val)


post(bst.root)




