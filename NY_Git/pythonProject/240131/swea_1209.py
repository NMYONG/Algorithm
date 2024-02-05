import sys
sys.stdin = open("1209.txt", "r")

# 최댓값을 구하는 함수
def my_max(arr):
    maxV = arr[0]
    for i in arr:
        if i >= maxV:
            maxV = i
    return maxV


for tc in range(1, 11):
    N = int(input())
    # 값 입력받기
    arr = [list(map(int, input().split())) for _ in range(100)]

    # row의 합 구하기
    sumV = 0
    sum_lst = []
    N = len(arr)


    # row
    for i in range(N):
        for j in range(N):
            sumV += arr[i][j]
        sum_lst.append(sumV)
        sumV = 0

    # col
    for j in range(N):
        for i in range(N):
            sumV += arr[i][j]
        sum_lst.append(sumV)
        sumV = 0

    # 우하강 대각선
    for i in range(N):
        sumV += arr[i][i]
    sum_lst.append(sumV)
    sumV = 0

    # 좌하강 대각선
    for i in range(N):
        sumV += arr[i][N-1-i]
    sum_lst.append(sumV)
    sumV = 0

    print(f'#{tc} {my_max(sum_lst)}')
