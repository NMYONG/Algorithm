from collections import deque

def bfs(start):
    global depthCnt
    q = deque()
    visited = [0] * (N + 1)

    q.append((start, 0))

    while q:
        isLeaf = True
        node, depth = q.popleft()
        visited[node] = 1

        for child in adj[node]:
            if not visited[child]:
                isLeaf = False
                q.append((child, depth + 1))

        if isLeaf:
            depthCnt += depth

N = int(input())
adj = [[] for _ in range(N+1)]
depthCnt = 0

for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

bfs(1)

if depthCnt % 2:
    print('Yes')
else:
    print('No')
