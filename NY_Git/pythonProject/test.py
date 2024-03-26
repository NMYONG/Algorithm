def dfs(idx, sum_height):
    global ans

    if sum_height >= B:
        ans = min(ans, sum_height)
        return

    if idx == N:
        return

    dfs(idx + 1, sum_height + lst[idx])
    dfs(idx + 1, sum_height)

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = float('inf')
    dfs(0, 0)
    print(f'#{tc} {abs(ans-B)}')