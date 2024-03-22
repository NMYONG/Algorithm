# month를 level로 생각한다.
# 매달 1일에 1가지 종류의 회원권밖에 살 수 없다.

# DFS
def dfs(idx, sum_cost):
    global ans

    # 기저조건
    # 1. 12월까지 다 봤네? 종료
    if idx > 12:
        ans = min(ans, sum_cost)
        return

    # 2. 이미 최소값을 넘어갔네? 종료
    if sum_cost >= ans:
        return

    # 모두 1일권으로 구매
    dfs(idx + 1, sum_cost + day * lst[idx])
    # 1달권 구매
    dfs(idx + 1, sum_cost + month)
    # 3달권 구매
    dfs(idx + 3, sum_cost + month3)
    # 1년권 구매
    dfs(idx + 12, sum_cost + year)


T = int(input())
for tc in range(1, T + 1):
    day, month, month3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))
    ans = 3000 * 12
    dfs(1, 0)

    print(f'#{tc} {ans}')





# DP
T = int(input())
for tc in range(1, T + 1):
    day, month, month3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))

    D = [0] * 13
    for i in range(1, 13):
        # 가능한 4가지 방법 중 i달의 최소 비용
        # 일간권
        mn = D[i - 1] + lst[i] * day
        # 월간권과 비교
        mn = min(mn, D[i - 1] + month)
        # 3개월권과 비교
        if i >= 3:
            mn = min(mn, D[i - 3] + month3)
        # 연간권과 비교
        if i >= 12:
            mn = min(mn, D[i - 12] + year)

        D[i] = mn

    ans = D[12]

    print(f'#{tc} {ans}')
