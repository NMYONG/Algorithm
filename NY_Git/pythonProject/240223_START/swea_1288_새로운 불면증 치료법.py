T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = []
    cnt = 0
    i = 1

    while len(lst) != 10:
        for c in str(N*i):
            lst.append(int(c))

        lst = set(lst)
        cnt += 1
        i += 1
        lst = list(lst)

    print(f'#{tc} {cnt*N}')
