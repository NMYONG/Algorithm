def bfs(si, sj, ei, ej):
    q = []
    v = [[INF] * N for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = 0  # 값 초기화

    while q:
        ci, cj = q.pop(0)
        for dj, di in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] > v[ci][cj] + 1 + max(arr[ni][nj] - arr[ci][cj], 0):
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1 + max(arr[ni][nj] - arr[ci][cj], 0)
    return v[ei][ej]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    INF = int(1e6)

    ans = bfs(0, 0, N - 1, N - 1)

    print(f'#{tc} {ans}')
