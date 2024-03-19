def dfs(n, cnt, power):
    global ans

    if cnt >= ans:
        return

    if n == N:
        ans = min(ans, cnt)
        return

    # 유망한 답이 먼저 나오는 방향으로 호출
    # 교체하지 않는 경우
    if power > 0:
        dfs(n + 1, cnt, power - 1)
    # 교체하는 경우
    dfs(n + 1, cnt + 1, lst[n] - 1)


T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst[0]
    ans = N  # 모든 정류장에서 교체 할 경우 (최대값)

    # 2번 정류장에서 시작함
    # 1번 정류장에서는 교체회수 포함 x
    # 배터리 양은 1번 정류장 -1
    dfs(2, 0, lst[1] - 1)
    print(f'#{tc} {ans}')




# 1부터 시작하는 경우
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
