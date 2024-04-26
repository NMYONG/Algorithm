def dfs(n, lst):
    global max_sum

    if n == 3:
        if sum(lst) <= M:
            if sum(lst) > max_sum :
                max_sum = sum(lst)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(n+1, lst + [numList[i]])
            visited[i] = 0

N, M = map(int, input().split())
numList = list(map(int, input().split()))

ans = []
visited = [0] * N

max_sum  = 0
dfs(0, [])

print(max_sum)
