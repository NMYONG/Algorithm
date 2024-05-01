def dfs(start, end, sumLength):
    global totalLength
    if start == end:
        totalLength = sumLength
        return

    visited[start] = 1

    for c, l in adj[start]:
        if not visited[c]:
            dfs(c, end, sumLength + l)


N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, l = map(int, input().split())
    adj[a].append((b, l))
    adj[b].append((a, l))

for _ in range(M):
    visited = [0] * (N + 1)
    totalLength = 0

    start, end = map(int, input().split())
    if start > end:
        start, end = end, start
    dfs(start, end, 0)

    print(totalLength)

# print(adj)
