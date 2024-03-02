# 두 개의 배열을 활용해서 모든 경우의 수 찾기
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    # 입력 받았으면 입력 제대로 받았는지 확인
    # 긴 배열을 A, 짧은 배열을 B에 위치
    # 긴 배열의 길이 N, 짧은 배열의 길이 M
    if N < M:
        A, B = B, A
        N, M = M, N
    # 합의 최대값을 저장할 변수
    # 변수의 초기값? >> 가장 작은값(임의로 작성해야 할 경우는 최대한 작게)
    sum_max = -0xffffffff
    # B와 A를 비교하기 위한 A배열의 시작점 : i
    for i in range(N-M+1):
        tmp_sum = 0
        #짧은 배열의 요소를 순회하면서
        # 마주보고 있는 긴배열의 요소와 곱의 결과를 모두 더하기
        for j in range(M):
            tmp_sum += A[i+j]*B[j]
        # 방금 마주보고 있는 요소끼리의 곱의 합이 원래 알고 있던 최대값 보다 크면 저장
        if sum_max < tmp_sum:
            sum_max = tmp_sum

    print(f'#{tc} {sum_max}')




# 내 풀이
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if len(A) > len(B):
        N, M = M, N
        A, B = B, A

    max_sum = -999999999
    for i in range(M-N+1):
        sum_v = 0
        for j in range(N):
            sum_v += A[j] * B[i+j]
        if sum_v > max_sum:
            max_sum = sum_v

    print(f'#{tc} {max_sum}')