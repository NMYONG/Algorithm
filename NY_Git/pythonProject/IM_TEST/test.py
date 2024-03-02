T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    candidate = 0
    for row in range(N):
        for col in range(M):
            cnt = 0
            land = arr[row][col]

            delta = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
            for dr, dc in delta:
                new_r = row + dr
                new_c = col + dc

                if 0 <= new_r < N and 0 <= new_c < M and arr[new_r][new_c] < land:
                    cnt += 1

            if cnt >= 4:
                candidate += 1

    print(f'#{tc} {candidate}')