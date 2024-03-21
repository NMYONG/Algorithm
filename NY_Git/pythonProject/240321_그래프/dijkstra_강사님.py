'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

INF = int(1e6)
def dijk(now):
    U = []
    D = [INF] * V

    D[now] = 0
    while len(U) < V:
        minV = INF
        for i in range(V):
            if i in U: continue
            if D[i] < minV:
                minV = D[i]
                now = i

        U.append(now)

        for i in range(V):
            if i in U: continue
            if G[now][i]:
                D[i] = min(D[i], D[now]+G[now][i])

    print(U, D)

V, E = map(int, input().split())
G = [[0]*V for _ in range(V)]

for i in range(E):
    v1, v2, w = map(int, input().split())
    G[v1][v2] = w

# print(G)
dijk(0)
