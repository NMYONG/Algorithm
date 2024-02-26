from collections import deque

def dfs(start):
    STACK = []
    visited = [False] * (N+1)

    STACK.append(start)
    visited[start] = True

    while STACK:
        v = STACK.pop()
        print(v, end=' ')

        for w in sorted(G[v]):
            if not visited[w]:
                STACK.append(w)
                visited[w] = True

def bfs(start):
    queue = deque()
    visited = [False] * (N+1)

    queue.append(start)
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for w in sorted(G[v]):
            if not visited[w]:
                queue.append(w)
                visited[w] = True

N, M, V = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())

    G[v1].append(v2)
    G[v2].append(v1)

print(G)
dfs(V)
print()
bfs(V)