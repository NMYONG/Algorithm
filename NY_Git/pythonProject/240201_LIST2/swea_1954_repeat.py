# 1. test case 입력받기
# 2. N 입력받기
# 3. N*N 빈 배열 생성하기
# 4. 3에 N*N 까지 1~N*N 값 넣어주기
# 5. 새로운 값을 입력할 N*N 빈 배열 생성하기
# 6. 인덱스, 첫번째 값, 델타, 델타 인덱스 초기화하기
# 7. 차례대로 입력하고 특정 조건에서 델타를 사용해 방향전환


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    start_num = 1
    arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr[i][j] = start_num
            start_num += 1

    new_arr = [[0] * N for _ in range(N)]

    value = 0
    row = 0
    col = 0

    dr = [0, 1, 0, -1]# 우, 하, 좌, 상 순서
    dc = [1, 0, -1, 0]
    d = 0

    for _ in range(N*N):
        value += 1
        new_arr[row][col] = value

        new_row = row + dr[d]
        new_col = col + dc[d]

        # 조건 설정하기 = new_row, new_col이 범위를 벗어났거나 다음 인덱스 자리에 값이 있는 경우 방향 전환
        if not (0 <= new_row < N and 0 <= new_col < N) or (new_arr[new_row][new_col] != 0):
            d = (d+1)%4

            new_row = row + dr[d]
            new_col = col + dc[d]

        row = new_row
        col = new_col

    print(f'#{tc}')
    for row in range(N):
        for col in range(N):
            print(new_arr[row][col], end=' ')
        print()