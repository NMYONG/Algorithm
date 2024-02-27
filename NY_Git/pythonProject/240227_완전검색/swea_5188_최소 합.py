def recu(row, col, mid_sum):
    global min_v

    if row == N - 1 and col == N - 1:  # 또는 num == 2*N-1 로 해도 됨
        if mid_sum < min_v:
            min_v = mid_sum

    if col + 1 < N:
        recu(row, col + 1, mid_sum+ARR[row][col+1])  # 오른쪽가고
    if row + 1 < N:
        recu(row + 1, col, mid_sum+ARR[row+1][col])  # 아래 가고


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]
    path = []
    min_v = 10 * N
    recu(0, 0, ARR[0][0])
    print(f'#{tc} {min_v}')

    # 오른쪽이나 아래로만 이동 가능, 오른쪽(0,1) / 아래(1,0)
    # 3x3인 경우, (0,0) -> (0,1) 오른쪽 -> (0,2), (1,1)




