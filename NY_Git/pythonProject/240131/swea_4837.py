# 리스트 컴프리헨션
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())
for test_case in range(1, T+1):

    N, K = map(int, (input().split()))
    a = len(A) # A의 길이
    result = 0

    for i in range(1<<a): # 전체 부분집합 구하기
        current_subset = [A[j] for j in range(len(A)) if (i & (1 << j)) > 0]
        if len(current_subset) == N and sum(current_subset) == K: # 조건설정
            result += 1

    print(f'#{test_case} {result}')


# for문
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    a = len(A)  # A의 길이
    result = 0

    for i in range(1 << a):
        current_subset = []
        for j in range(len(A)):
            if (i & (1 << j)) > 0:
                current_subset.append(A[j])

        if len(current_subset) == N and sum(current_subset) == K:
            result += 1

    print(f'#{test_case} {result}')
