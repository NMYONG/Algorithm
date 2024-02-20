# 중위 순회

def inOrder(root):
    global answer

    if len(TREE[root]) >= 1:
        inOrder(TREE[root][0])
    # print(root, end=' ')
    answer.append(DATA[root-1][1])
    if len(TREE[root]) >= 2:
        inOrder(TREE[root][1])


for tc in range(10):
    N = int(input())
    TREE = [[] for _ in range(N+1)]
    answer = []

    # DATA 입력
    DATA = []
    for _ in range(N):
        DATA.append(list(input().split()))
    # print('DATA:', DATA)

    # 입력에 맞도록 간선 정보 리스트 생성
    lst = []
    for i in range(len(DATA)):
        if len(DATA[i]) == 4:
            lst.append(int(DATA[i][0]))
            lst.append(int(DATA[i][2]))
            lst.append(int(DATA[i][0]))
            lst.append(int(DATA[i][3]))
        elif len(DATA[i]) == 3:
            lst.append(int(DATA[i][0]))
            lst.append(int(DATA[i][2]))
    # print('lst:', lst)

    # TREE 생성
    for idx in range(0, len(lst), 2):
        p = lst[idx]
        c = lst[idx+1]

        TREE[p].append(c)
    # print('TREE:', TREE)

    inOrder(1)
    result = ''.join(answer)

    print(f'#{tc+1} {result}')