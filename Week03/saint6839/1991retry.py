
import sys

N = int(sys.stdin.readline())
graph = {}

for _ in range(N):
    root, left, right = map(str, sys.stdin.readline().rstrip().split())
    graph[root] = [root, left, right]

def preorder_traversal(node):
    print(node[0], end='')
    if node[1] != '.':
        preorder_traversal(graph[node[1]])
    if node[2] != '.':
        preorder_traversal(graph[node[2]])


def inorder_traversal(node):
    if node[1] != '.':
        inorder_traversal(graph[node[1]])
    print(node[0], end='')
    if node[2] != '.':
        inorder_traversal(graph[node[2]])
def postorder_traversal(node):
    if node[1] != '.':
        postorder_traversal(graph[node[1]])
    if node[2] != '.':
        postorder_traversal(graph[node[2]])
    print(node[0], end='')

preorder_traversal(graph['A'])
print()
inorder_traversal(graph['A'])
print()
postorder_traversal(graph['A'])