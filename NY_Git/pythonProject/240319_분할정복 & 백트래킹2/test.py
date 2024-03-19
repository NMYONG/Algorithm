def dfs(n, cnt, power):
    global ans

    if cnt >= ans:
        return

    if n == N:
        ans = min(ans, cnt)
        return

    if power > 0:
        dfs(n + 1, cnt, power - 1)
    dfs(n + 1, cnt + 1, lst[n] - 1)


T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst[0]
    ans = N

    dfs(1, 0, lst[1])
    print(f'#{tc} {ans}')
