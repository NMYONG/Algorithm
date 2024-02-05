# import sys
# sys.stdin = open('16268.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum_lst = []
    for row in range(N):
        for col in range(M):
            sum_value = arr[row][col]

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r = row + dr
                new_c = col + dc

                if (0 <= new_r < N) and (0 <= new_c < M):
                    sum_value += arr[new_r][new_c]

            sum_lst.append(sum_value)

    print(f'#{tc} {max(sum_lst)}')
