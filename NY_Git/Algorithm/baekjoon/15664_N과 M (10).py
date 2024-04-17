def dfs(n, start, lst):
    if n == M:
        ans.append(lst)
        return

    temp = 0
    for i in range(start, len(numbers)):
        if temp != numbers[i]:
            if not visited[i]:
                visited[i] = 1
                dfs(n + 1, i, lst + [numbers[i]])
                visited[i] = 0
                temp = numbers[i]

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

ans = []
visited = [0] * len(numbers)

dfs(0, 0, [])

for i in ans:
    print(*i)