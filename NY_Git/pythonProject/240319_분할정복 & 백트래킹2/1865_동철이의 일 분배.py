def dfs(level, times):
    global ans

    if ans >= times : return

    if level == N:
        ans = max(ans, times)
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(level + 1, times * arr[level][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            arr[r][c] *= 0.01

    ans = 0
    visited = [0] * N

    dfs(0, 1)
    print(f'#{tc} {ans*100:.6f}')