# 메모이제이션을 활용한 동적 프로그래밍 예시 - 피보나치 수열

def fibonacci_memo(n, memo={}):
    if n <= 1:
        return n

    if n not in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    return memo[n]

# 테스트
result = fibonacci_memo(5)
print(result)
