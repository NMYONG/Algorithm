# subtree

def preOrder(root):
    global cnt
    cnt += 1
    if len(TREE[root]) >= 1:
        preOrder(TREE[root][0])
    if len(TREE[root]) >= 2:
        preOrder(TREE[root][1])

    return cnt

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split()) # 간선의 수, 시작 노드
    lst = list(map(int, input().split()))

    V = E + 1 # 노드의 개수
    TREE = [[] for _ in range(V+1)] # 노드의 개수 +1 만큼 생성
    cnt = 0

    for idx in range(0, len(lst), 2):
        p = lst[idx]
        c = lst[idx+1]

        TREE[p].append(c)

    answer = preOrder(N)

    print(f'#{tc} {answer}')
