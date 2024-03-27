def dfs(n, a_lst, b_lst):
    global ans

    if n == N:
        if len(a_lst) == N // 2:
            a_sum = b_sum = 0  # 음식 맛의 합을 저장할 변수
            for i in range(N // 2):
                for j in range(N // 2):
                    a_sum += arr[a_lst[i]][a_lst[j]]
                    b_sum += arr[b_lst[i]][b_lst[j]]
            ans = min(ans, abs(a_sum - b_sum))
        return

    dfs(n + 1, a_lst + [n], b_lst)  # a 음식에 추가
    dfs(n + 1, a_lst, b_lst + [n])  # b 음식에 추가


# 입력
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 최소값 변수 초기화
    ans = float('inf')

    # 함수 호출
    dfs(0, [], [])

    print(f'#{tc} {ans}')
