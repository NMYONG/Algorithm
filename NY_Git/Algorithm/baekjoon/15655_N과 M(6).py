def dfs(n, s, lst):
    if n == M:
        ans.append(lst)
        return

    for i in range(s, N):
        dfs(n+1, i + 1, lst+[num_lst[i]])

N, M = map(int, input().split())
num_lst = sorted(list(map(int, input().split())))

ans = []

dfs(0, 0, [])

for i in ans:
    print(*i)