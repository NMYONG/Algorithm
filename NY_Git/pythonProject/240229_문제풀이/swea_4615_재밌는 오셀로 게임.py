'''
row, col, color =
if color == 'W':
    color_r = 'B'
else:
    color_r = 'W'

for dr, dc in [8방향]:
    while 범위비교, 값 비교(나하고 다른 색 인 동안):
        new_r, new_c =

    if 값을 찾아서 빠져 나온 경우:
        while 원래 좌표가 아닌 동안:
            역방향으로 뒤집기
'''

# 정준 코드
def stepover(row, col):
    for k in range(8):
        st_color = board[row][col]
        newR = row + ni[k]
        newC = col + nj[k]

        if st_color == 1:
            color_r = 2
        else:
            color_r = 1

        while 0 <= newR < N and 0 <= newC < N and board[newR][newC] == color_r: # 다른색이면
            # 판에 돌이 들어있지 않으면 반복문 종료
            if not board[newR][newC]:
                break

            newR += ni[k]
            newC += nj[k]

        if 0 <= newR < N and 0 <= newC < N and board[newR][newC] == st_color:
            while newR != row or newC != col:
                newR -= ni[k]
                newC -= nj[k]
                board[newR][newC] = st_color

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    board = [[0] * N for _ in range(N)]
    board[(N-1)//2][(N-1)//2] = board[(N-1)//2 + 1][(N-1)//2 + 1] = 2
    board[(N-1)//2 + 1][(N-1)//2] = board[(N-1)//2][(N-1)//2 + 1] = 1

    # 상 우 하 좌
    ni = [-1, -1, 0, 1, 1, 1, 0, -1]
    nj = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(M):
        c, r, dol = arr[i]
        r -= 1
        c -= 1
        board[r][c] = dol
        stepover(r, c)

    cnt_1 = 0
    cnt_2 = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt_1 += 1
            elif board[i][j] == 2:
                cnt_2 += 1

    print(f'#{tc} {cnt_1} {cnt_2}')