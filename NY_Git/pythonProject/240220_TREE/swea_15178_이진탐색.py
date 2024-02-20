# 이진탐색
def inOrder(root):
    global value

    if root <= N: # 가상노드가 아니고 정식 노드이면
        inOrder(root*2)
        TREE[root] = value
        value += 1
        # print(root)
        inOrder(root*2 + 1)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    TREE = [0] * (N+1)
    value = 1

    inOrder(1)

    print(f'#{tc} {TREE[1]} {TREE[N//2]}')
