def postOrder(root):
    if root <= N:
        if str(TREE[root][0]).isdigit():
            return TREE[root][0]
        else:
            v1 = postOrder(root*2)
            v2 = postOrder(root*2 + 1)

            operator = TREE[root][0]
            if operator == '+':
                return v1 + v2
            elif operator == '-':
                return v1 - v2
            elif operator == '*':
                return v1 * v2
            elif operator == '/':
                return v1 // v2


for tc in range(1, 11):
    N = int(input())
    DATA = [] # 입력
    lst = [] # 트리의 간선정보
    TREE = [[] for _ in range(N+1)]

    for _ in range(N):
        DATA.append(list(input().split()))

    for i in range(len(DATA)):
        if len(DATA[i]) == 4:
            lst.append(int(DATA[i][0]))
            lst.append(int(DATA[i][2]))
            lst.append(int(DATA[i][0]))
            lst.append(int(DATA[i][3]))
        if len(DATA[i]) == 4 and not DATA[i][1].isdigit():
            TREE[int(DATA[i][0])] = [DATA[i][1]]

        else:
            TREE[int(DATA[i][0])] = [int(DATA[i][1])]

    print(f'#{tc} {postOrder(1)}')


