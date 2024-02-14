# 바텀업 방식을 활용한 동적 프로그래밍 예시 - 피보나치 수열

def fibonacci_bottom_up(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# 테스트
result = fibonacci_bottom_up(5)
print(result)
