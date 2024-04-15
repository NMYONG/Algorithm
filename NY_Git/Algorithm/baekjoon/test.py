N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0

for i in range(N):
    flag = 0
    for j in range(N-1):
        # 현재 숫자와 다음 숫자가 같으면
        if arr[i][j] == arr[i][j+1]:
            continue

        # 다음 숫자가 더 크고 그 차이가 1이하라면
        elif arr[i][j] < arr[i][j+1] and (arr[i][j+1] - arr[i][j]) <= 1:
            # L만큼 길이가 존재하는지 검사
            try:
                status = True # 상태를 저장할 수 있는 변수
                # L 길이에 대해서
                for l in range(1, L+1):
                    if arr[i][j+1-i] == arr[i][j+1] - 1:
                        status = True
                    else:
                        flag = 0
                        break
                if status:
                    flag = 1
            except IndexError: # 인덱스 에러가 나면 경사로 만들 수 없다.
                flag = 0

        if flag:
            answer += 1

        # 다음 숫자가 더 작고 그 차이가 1이하라면
        elif arr[i][j] > arr[i][j+1] and (arr[i][j] - arr[i][j+1]) <= 1:
            pass