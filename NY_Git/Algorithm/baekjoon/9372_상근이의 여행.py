import sys
input = sys.stdin.readline

def dfs(node, cnt):
    visited[node] = 1

    for c in adj[node]:
        if not visited[c]:
            cnt = dfs(c, cnt + 1)
    return cnt

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    adj = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    visited = [0] * (N+1)
    print(dfs(1, 0))