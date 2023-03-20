# 분류 : accepted

# 1991 트리순회

# 블로그 : https://blog.naver.com/ndb796/221233560789

# ----------딕셔너리로 구현 -------------------
# # 입력받고
import sys
input = sys.stdin.readline

N = int(input().rstrip())
tree = {}
for _ in range(N):
    root, left, right = input().rstrip().split()
    tree[root] = (left, right)
# print(tree)

# tree = {'A' : ('B', 'C'),
#        'B' : ('D', '.'),
#        'C' : ('E', 'F'),
#        'E' : ('.', '.'),
#        'F' : ('.', 'G'),
#        'D' : ('.', '.'),
#        'G' : ('.', '.'),}

# 솔루션

# 전위순회 preorder 노드 방문 > 왼쪽 자식 > 오른쪽 자식
def preorder(n):
    if n != '.':
        print(n, end="")
        preorder(tree[n][0])
        preorder(tree[n][1])

# 중위순회 inorder왼쪽 자식 > 노드 방문 > 오른쪽 자식
def inorder(n):
    if n != '.':
        inorder(tree[n][0])
        print(n, end="")
        inorder(tree[n][1])

# 후위순회 postorder왼쪽 자식 > 오른쪽 자식 > 노드 방문
def postorder(n):
    if n != '.':
        postorder(tree[n][0])
        postorder(tree[n][1])
        print(n, end="")
        
# 출력

preorder('A')
print()
inorder('A')
print()
postorder('A')

# -------------- class로 구현 -----------------
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회
def pre_order(node):
    print(node.data, end='')
    if node.left_node != '.':
        pre_order(tree[node.left_node])
    if node.right_node != '.':
        pre_order(tree[node.right_node])

# 중위 순회
def in_order(node):
    if node.left_node != '.':
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != '.':
        in_order(tree[node.right_node])

# 후위 순회
def post_order(node):
    if node.left_node != '.':
        post_order(tree[node.left_node])
    if node.right_node != '.':
        post_order(tree[node.right_node])
    print(node.data, end='')


tree = {}
N = int(input().rstrip())
for _ in range(N):
    data, left_node, right_node = input().rstrip().split()
    # print(data, left_node, right_node)
    tree[data] = Node(data, left_node, right_node)

# print(tree)

root = tree['A']
pre_order(root)
print()
in_order(root)
print()
post_order(root)