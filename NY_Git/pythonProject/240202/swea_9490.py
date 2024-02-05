T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for row in range(N):
        for col in range(M):
            sum_v = arr[row][col]

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                for dd in range(1, arr[row][col]+1):
                    new_row = row + dr * dd
                    new_col = col + dc * dd

                    if 0<=new_row<N and 0<=new_col<M:
                        sum_v += arr[new_row][new_col]
                if max_v < sum_v:
                    max_v = sum_v


    print(f'#{tc} {max_v}')