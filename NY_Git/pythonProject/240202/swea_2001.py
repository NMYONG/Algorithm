import sys
sys.stdin = open('2001.txt', 'r')

# 정답
T = int(input())  # 테스트 케이스의 수 입력

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum_flies = []  # 각 위치에서의 파리 합을 저장할 리스트

    # 주어진 배열을 순회하며 파리채를 내리쳐 최대한 많은 파리를 죽이는 영역을 찾기
    for row in range(N):
        for col in range(N):
            total_flies = 0
            # 파리채가 내려쳐진 영역을 순회하여 파리의 수를 더하기
            for i in range(M):
                for j in range(M):
                    # 배열 범위를 벗어나지 않도록 조건 추가
                    if row + i < N and col + j < N:
                        total_flies += arr[row + i][col + j]
            sum_flies.append(total_flies)

    result = max(sum_flies)  # 최대값 찾기
    print(f'#{tc} {result}')  # 결과 출력





# 내 풀이
T = int(input())

for tc in range(1,  T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    catch = []

    for i in range(N):
        for j in range(N):
            if 0 <= i <= N-M and 0 <= j <= N-M:
                temp = 0
                for r in range(M):
                    for c in range(M):
                        temp += (arr[i+r][j+c])
                catch.append(temp)

    print(f'#{tc} {max(catch)}')