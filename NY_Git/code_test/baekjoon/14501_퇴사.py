n = int(input())
T, P = [0 for i in range(n+1)], [0 for i in range(n+1)]
for i in range(n):
    T[i], P[i] = map(int, input().split())

# dp[i]는 i번째날까지 일을 했을 때, 최대값이다.
dp =[0 for i in range(n+1)]

for i in range(n-2, -1, -1):      # 역순으로 진행
    if T[i]+i <= n:       # 날짜를 초과하지 않을 경우.
        dp[i] = max(P[i] + dp[i + T[i]], dp[i+1])
    else:                 # 날짜를 초과할 경우.
        dp[i] = dp[i+1]
print(dp[0])



# 완전 탐색

def dfs(idx, profit):
    global answer

    if idx >= N:                        # 종료조건 설정
        answer = max(answer, profit)    # 모든 경우에 대해서 실행하므로 최댓값
        return

    if N >= idx + T[idx]:               # 가능한 경우 : idx는 idx+T[idx], profit은 profit+P[idx]
        dfs(idx+T[idx], profit+P[idx])

    dfs(idx+1, profit)                  # 불가능 한 경우 : idx는 +1, profit은 그대로


N = int(input())
T, P = [0 for _ in range(N)], [0 for _ in range(N)]

for i in range(N):
    T[i], P[i] = map(int, input().split())

answer = 0

dfs(0, 0)
print(answer)