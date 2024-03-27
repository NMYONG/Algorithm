def dfs(level, start, link):
    global ans

    if level == N:
        if len(start) == N // 2:
            start_sum = 0
            link_sum = 0
            for i in range(N // 2):
                for j in range(N // 2):
                    start_sum += arr[start[i]][start[j]]
                    link_sum += arr[link[i]][link[j]]
            ans = min(ans, abs(start_sum - link_sum))
        return

    dfs(level + 1, start + [level], link)
    dfs(level + 1, start, link + [level])


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = float('inf')

dfs(0, [], [])

print(ans)
