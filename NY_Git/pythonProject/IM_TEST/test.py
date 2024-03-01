T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if M > N:
        A, B = B, A
        N, M = M, N

    max_sum = -99999999
    for j in range(N-M+1):
        sum = 0
        for i in range(M):
            sum += A[j+i] * B[i]
        if sum > max_sum:
            max_sum = sum

    print(f'#{tc} {max_sum}')

