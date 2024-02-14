def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(7))



# 강사님 설명
# 피보나치 -memoziation
n = 5
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
...

def fib_m(n):
    if n > 1 and memo[n] == 0:
        memo[n] = fib_m(n-1) + fib_m(n-1)
        # return fib_m(n-1) + fib_m(n-1)
    else:
        return memo[n]

print(fib_m(n))


# dp
dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])