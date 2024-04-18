def dfs(start, end):
    global cnt

    if start == end:
        return

    visited[start] = 1

    for c in adj[start]:
        if not visited[c]:
            dfs(c, end)


    return -1

N = int(input())
A, B = map(int, input().split())
M = int(input())
adj = [[] for _ in range(N + 1)]

for _ in range(N - 2):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

# print(adj)
visited = [0] * (N + 1)
cnt = 0
dfs(A, B)

print(cnt)