class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left  = left
        self.right = right

import sys

input = sys.stdin.readline

n = int(input())

tree = {}

for _ in range(n):
    v, l, r= input().strip().split()

    if l == '.':
        l = None
    if r == '.':
        r = None
    
    tree[v] = Node(v, l ,r)

def pre(root):
    print(root.value, sep="", end="")
    if root.left:
        pre(tree[root.left])
    if root.right:
        pre(tree[root.right])

pre(tree['A'])
print()

def ino(root):
    if root.left:
        ino(tree[root.left])
    print(root.value, sep="", end="")
    if root.right:
        ino(tree[root.right])

ino(tree['A'])
print()

def pos(root):
    if root.left:
        pos(tree[root.left])
    if root.right:
        pos(tree[root.right])
    print(root.value, sep="", end="")

pos(tree['A'])
print()


    

    




