T = int(input())

for tc in range(1, T+1):
    N = int(input())

    dp = [0] * ((N//10) + 1)

    # 점화식 규칙 찾기 dp[i] = dp[i-1] + 2 * dp[i-2]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 3
    dp[3] = 5

    for i in range(4, (N//10) + 1):
        dp[i] = dp[i-1] + 2 * dp[i-2]

    print(f'#{tc} {dp[N//10]}')