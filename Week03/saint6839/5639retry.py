import sys
sys.setrecursionlimit(10**6)
values = []
while True:
    try:
        values.append(int(sys.stdin.readline()))
    except:
        break

def postorder_traversal(start, end):
    if start > end:
        return

    mid = end + 1
    for i in range(start+1, end+1):
        if values[i] > values[start]:
            mid = i
            break
    postorder_traversal(start+1, mid-1)
    postorder_traversal(mid, end)
    print(values[start])

postorder_traversal(0, len(values)-1)
