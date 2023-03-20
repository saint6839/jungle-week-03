import sys
sys.setrecursionlimit(10**6)
nodes = []

while True:
    try:
        nodes.append(int(sys.stdin.readline()))
    except:
        break


def postorder_traversal(start, end):
    if start > end:
        return

    mid = end + 1

    for i in range(start+1, end + 1):
        if nodes[start] < nodes[i]:
            mid = i
            break

    postorder_traversal(start + 1, mid - 1)
    postorder_traversal(mid, end)
    print(nodes[start])

postorder_traversal(0, len(nodes) - 1)