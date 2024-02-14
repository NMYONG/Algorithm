
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    # n개만큼 색칠 정보가 담긴 배열 생성
    arr_list = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    # 빈 배열 생성
    empty_arr = [[0] * 10 for _ in range(10)]

    # 배열을 돌며
    for arr in arr_list:
        for i in range(arr[0], arr[2]+1):
            for j in range(arr[1], arr[3]+1):
                empty_arr[i][j] += arr[4]

    # 전체 배열을 돌며 3을 카운트
    for row in empty_arr:
        for element in row:
            if element == 3:
                cnt += 1

    print(f'#{tc} {cnt}')
