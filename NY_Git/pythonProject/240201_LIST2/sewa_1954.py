# value보다 큰것 중 제일 작은 값 찾기
# def getMin(value):
#     min_v = 1e10
#     for r in range(N):
#         for c in range(N): # value보다 큰 수 중 제일 작은 값 찾기
#             if arr[r][c] < min_v  and arr[r][c] > value:
#                 min_v = arr[r][c]
#     return min_v

T = int(input())
for tc in range(1, T+1):

    N = int(input())

    arr = [[0] * N for _ in range(N)]
    num = 1

    for i in range(N):
        for j in range(N):
            arr[i][j] = num
            num += 1


    new_arr = [[0] * N for _ in range(N)] # 값을 넣어줄 새로운 빈 배열 생성

    value = 0
    row = 0
    col = 0
    dr = [0, 1, 0, -1] # 우, 하, 좌, 상 (방향이 정해져있음)
    dc = [1, 0, -1, 0]
    d = 0

    for _ in range(N*N): # 배열 전체 원소의 갯수만큼 반복
        value += 1
        new_arr[row][col] = value

        new_r = row + dr[d]
        new_c = col + dc[d]

        if not (0 <= new_r < N and 0 <= new_c < N) or (new_arr[new_r][new_c] != 0): # 범위가 벗어났거나 값이 있으면
            d = (d+1)%4 # 방향 전환 (0, 1, 2, 3) 반복

            new_r = row + dr[d] # 새로운 값을 입력할 인덱스의 자리
            new_c = col + dc[d]

        row = new_r # 인덱스 값 유지
        col = new_c

    print(f'#{tc}')
    for row in range(N):
        for col in range(N):
            print(new_arr[row][col], end=' ')
        print()