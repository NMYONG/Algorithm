def postOrder(root):
    if root*2 <= N: # 왼쪽 노드 범위 설정
        TREE[root] += postOrder(root*2)
    if root*2 + 1 <= N: # 오른족 노드 범위 설정
        TREE[root] += postOrder(root*2 + 1)

    return TREE[root]

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    TREE = [0] * (N+1)

    for _ in range(M):
        no, value = map(int, input().split())
        TREE[no] = value

    postOrder(1)
    print(f'#{tc} {TREE[L]}')
