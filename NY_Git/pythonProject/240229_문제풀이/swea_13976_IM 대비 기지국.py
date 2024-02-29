T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N+1)]

    house = 0
    for i in arr:
        house += i.count('H')

    for row in range(N+1):
        for col in range(N):

            if arr[row][col] == 'A':
                dr = [-1, 1, 0, 0]
                dc = [0, 0, -1, 1]
                power = 1
                for d in range(4):
                    for p in range(1, power+1):
                        new_row = row + dr[d] * p
                        new_col = col + dc[d] * p
                        if 0 <= new_row < N and 0 <= new_col < N+1:
                            if arr[new_row][new_col] == 'H':
                                house -= 1
                                arr[new_row][new_col] = 'X'

            if arr[row][col] == 'B':
                dr = [-1, 1, 0, 0]
                dc = [0, 0, -1, 1]
                power = 2
                for d in range(4):
                    for p in range(1, power+1):
                        new_row = row + dr[d] * p
                        new_col = col + dc[d] * p
                        if 0 <= new_row < N and 0 <= new_col < N+1:
                            if arr[new_row][new_col] == 'H':
                                house -= 1
                                arr[new_row][new_col] = 'X'


            if arr[row][col] == 'C':
                dr = [-1, 1, 0, 0]
                dc = [0, 0, -1, 1]
                power = 3
                for d in range(4):
                    for p in range(1, power+1):
                        new_row = row + dr[d] * p
                        new_col = col + dc[d] * p
                        if 0 <= new_row < N and 0 <= new_col < N+1:
                            if arr[new_row][new_col] == 'H':
                                house -= 1
                                arr[new_row][new_col] = 'X'


    print(f'#{tc} {house}')