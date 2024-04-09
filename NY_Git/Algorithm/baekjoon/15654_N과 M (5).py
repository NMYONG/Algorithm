def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return

    for i in range(len(num_lst)):
        if visited[i] == 0:
            visited[i] = 1
            dfs(n+1, lst + [num_lst[i]])
            visited[i] = 0

N, M = map(int, input().split())
num_lst = sorted(list(map(int, input().split())))
ans = []
visited = [0] * N

dfs(0, [])

for i in ans:
    print(*i)