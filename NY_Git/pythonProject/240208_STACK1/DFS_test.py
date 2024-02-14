# 백준 2606

'''
1 2
2 3
1 5
5 2
5 6
4 7
'''

def dfs(start):
    STACK = []
    visited = [False] * (N+1)

    STACK.append(start)
    visited[start] = True

    while STACK:
        v = STACK.pop()
        print(v)

        for w in G[v]:
            if not visited[w]:
                STACK.append(w)
                visited[w] = True


N = 7
l = 6
G = [[] for _ in range(N+1)]

for _ in range(l):
    a, b = map(int, input().split())

    G[a].append(b)
    G[b].append(a)

print(G) # [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
dfs(1)