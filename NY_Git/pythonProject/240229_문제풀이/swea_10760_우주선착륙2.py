import sys
sys.stdin = open('swea_10760_우주선착륙2.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    for row in range(N):
        for col in range(M):
            cnt = 0w
            land = arr[row][col]

            dr = [-1, -1, 0, 1, 1, 1, 0, -1]  # 가운데를 기준으로 좌상, 상, 우상, 우, 우하, 하, 좌하, 좌 방향
            dc = [0, 1, 1, 1, 0, -1, -1, -1]

            for dd in range(8):
                new_r = row + dr[dd]
                new_c = col + dc[dd]

                if 0 <= new_r < N and 0 <= new_c < M:
                    if arr[new_r][new_c] < land:
                        cnt += 1

            if cnt >= 4:
                answer += 1

    print(f'#{tc} {answer}')