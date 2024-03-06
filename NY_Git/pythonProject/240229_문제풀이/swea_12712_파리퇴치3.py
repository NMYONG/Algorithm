def plus(arr, M):
    max_num = 0
    for row in range(N):
        for col in range(N):
            num = arr[row][col]

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # 상, 하, 좌, 우
                for m in range(1, M):
                    new_row = row + dr * m
                    new_col = col + dc * m

                    if 0 <= new_row < N and 0 <= new_col < N:
                        num += arr[new_row][new_col]
            if num > max_num:
                max_num = num
    return max_num

def ex(arr, M):
    max_num = 0
    for row in range(N):
        for col in range(N):
            num = arr[row][col]

            for dr, dc in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:  # 좌상, 우상, 우하, 좌하
                for m in range(1, M):
                    new_row = row + dr * m
                    new_col = col + dc * m

                    if 0 <= new_row < N and 0 <= new_col < N:
                        num += arr[new_row][new_col]
            if num > max_num:
                max_num = num
    return max_num


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = max(plus(arr, M), ex(arr, M))
    print(f'#{tc} {result}')