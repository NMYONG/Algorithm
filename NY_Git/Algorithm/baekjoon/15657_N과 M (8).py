def dfs(n, s, lst):
    if n == M:
        ans.append(lst)
        return

    for i in range(s, N):
        dfs(n + 1, i, lst + [num_lst[i]])

N, M = map(int, input().split())
num_lst = list(map(int, input().split()))
num_lst.sort()

ans = []

dfs(0, 0, [])

for i in ans:
    print(*i)