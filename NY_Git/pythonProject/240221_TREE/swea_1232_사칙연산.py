def post_order(root):
    if not leftC[root]:
        return TREE[root]
    else:
        v1 = int(post_order(leftC[root]))
    if not rightC[root]:
        return TREE[root]
    else:
        v2 = int(post_order(rightC[root]))

        if TREE[root] == '+':
            TREE[root] = v1 + v2
            return TREE[root]
        elif TREE[root] == '-':
            TREE[root] = v1 - v2
            return TREE[root]
        elif TREE[root] == '*':
            TREE[root] = v1 * v2
            return TREE[root]
        else:
            TREE[root] = v1 // v2
            return TREE[root]

for tc in range(1, 11):
    N = int(input())
    DATA = [list(input().split()) for _ in range(N)]
    TREE = [0] * (N+1)
    # arr = [[] for _ in range(N+1)]
    leftC = [0] * (N+1)
    rightC = [0] * (N+1)

    for i in range(N):
        TREE[int(DATA[i][0])] = DATA[i][1]
        if len(DATA[i]) > 2:
            for j in range(2, len(DATA[i])):
                # arr[int(DATA[i][0])].append(int(DATA[i][j]))
                if leftC[int(DATA[i][0])] == 0:
                    leftC[int(DATA[i][0])] = int(DATA[i][j])
                else:
                    rightC[int(DATA[i][0])] = int(DATA[i][j])


    print(f'#{tc} {post_order(1)}')