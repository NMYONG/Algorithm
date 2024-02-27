def reculsive(row, col, mid_sum):
    global min_v

    if row == N-1 and col == N-1:
        if min_v > mid_sum:
            min_v = mid_sum

    if row+1 < N:
        reculsive(row+1, col, mid_sum + arr[row+1][col])
    if col+1 < N:
        reculsive(row, col+1, mid_sum + arr[row][col+1])


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_v = 10 * N

    reculsive(0, 0, arr[0][0])
    print(min_v)