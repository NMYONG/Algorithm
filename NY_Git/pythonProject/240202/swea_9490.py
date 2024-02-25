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







# 내 풀이
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = []
    for row in range(N):
        for col in range(M):
            num = arr[row][col]
            sum_num = 0
            sum_num += num

            for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # 상, 하, 좌, 우
                for i in range(1, num+1):
                    new_row = row + r*i
                    new_col = col + c*i

                    if (0 <= new_row < N) and (0 <= new_col < M):
                        sum_num += arr[new_row][new_col]

            answer.append(sum_num)

    print(f'#{tc} {max(answer)}')
