import sys

preorder_results = []
while True:
    try:
        preorder_results.append(int(sys.stdin.readline()))
    except:
        break

def postorder_traversal(start, end):
    if start > end:
        return

    mid = end + 1
    for i in range(start + 1, end + 1):
        # 부모 노드를 기준으로 값이 커지는 순간의 인덱스를 mid에 업데이트
        if preorder_results[i] > preorder_results[start]:
            mid = i
            break
    postorder_traversal(start + 1, mid - 1)
    postorder_traversal(mid, end)
    print(preorder_results[start])

postorder_traversal(0, len(preorder_results) - 1)


