def dfs(c):
    ans_dfs.append(c)
    visited[c] = 1

    for n in adj[c]:
        if visited[n] == 0:
            dfs(n)

def bfs(s):
    q = []
    q.append(s)

    ans_bfs.append(s)
    visited[s] = 1

    while q:
        c = q.pop(0)

        for n in adj[c]:
            if visited[n] == 0:
                q.append(n)
                ans_bfs.append(n)
                visited[n] = 1


N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

for i in adj:
    i.sort()

visited = [0] * (N+1)
ans_dfs = []
dfs(V)

visited = [0] * (N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)