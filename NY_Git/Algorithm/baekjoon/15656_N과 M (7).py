def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return

    for i in range(len(num_lst)):
        dfs(n +1 , lst + [num_lst[i]])


N, M = map(int, input().split())
num_lst = sorted(list(map(int, input().split())))
ans = []

dfs(0, [])

for i in ans:
    print(*i)