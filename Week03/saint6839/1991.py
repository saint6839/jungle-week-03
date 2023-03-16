import sys

N = int(sys.stdin.readline())
class Node():
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right

graph = {}
for _ in range(N):
    root, left, right = map(str, sys.stdin.readline().split())
    graph[root] = Node(root, left, right)

def preorder_traversal(node):
    print(node.root, end='')
    if node.left != '.':
        preorder_traversal(graph[node.left])
    if node.right != '.':
        preorder_traversal(graph[node.right])

def inorder_traversal(node):
    if node.left != '.':
        inorder_traversal(graph[node.left])
    print(node.root, end='')
    if node.right != '.':
        inorder_traversal(graph[node.right])

def postorder_traversal(node):
    if node.left != '.':
        postorder_traversal(graph[node.left])
    if node.right != '.':
        postorder_traversal(graph[node.right])
    print(node.root, end='')

root = 'A'
preorder_traversal(graph[root])
print()
inorder_traversal(graph[root])
print()
postorder_traversal(graph[root])

