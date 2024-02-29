# 내 코드
def omok(arr):
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 'o':
                for dr, dc in [(1, -1), (1, 0), (1, 1), (0, 1)]:
                    cnt = 1
                    for power in range(1, 5):
                        new_r = row + dr * power
                        new_c = col + dc * power
                        if 0 <= new_r < N and 0 <= new_c <N:
                            if arr[new_r][new_c] == 'o':
                                cnt += 1
                            else:
                                break
                        else:
                            break
                    if cnt == 5:
                        return 'YES'
    return 'NO'


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    answer = omok(arr)

    print(f'#{tc} {answer}')


# 강사님 코드
def omok(y, x):
    dy = [1, 0, 1, -1]
    dx = [0, 1, 1, 1]

    # 네 방향 탐색
    for bang in range(4):
        cnt = 1
        for power in range(1, 5):
            ny = y + (dy[bang] * power)
            nx = x + (dx[bang] * power)
            if not (0 < ny <= N and 0 < nx <= N):break
            if arr[ny][nx] == 'o': cnt += 1

            if cnt == 5:
                return True
    return False

def game_start():
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                if omok(r, c):
                    return 'YES'
    return 'NO'



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    result = game_start()

