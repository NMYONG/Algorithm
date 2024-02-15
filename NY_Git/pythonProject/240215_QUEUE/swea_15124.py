T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))

    for _ in range(M):
        Q.append(Q.pop(0))

    print(f'#{tc} {Q[0]}')