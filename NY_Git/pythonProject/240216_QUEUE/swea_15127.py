def bfs(S, G): # start, goal
    Q = []
    visited = [False] * (V+1) # 노드 + 1개만큼 생성

    Q.append(S)
    visited[S] = 1 # 방문하면 + 1

    while Q:
        v = Q.pop(0)

        if v == G:
            return visited[v] -1 # 1번 노드에서 시작했기 때문

        for w in Graph[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1 # 지금까지 visited + 1
    return 0


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split()) # V = 노드 개수, E = 간선 개수

    Graph = [[] for _ in range(V+1)]
    for e in range(E):
        n1, n2 = map(int, input().split()) # 간선 정보
        Graph[n1].append(n2)
        Graph[n2].append(n1)

    S, G = map(int, input().split()) # 출발지, 목적지

    print(f'#{tc} {bfs(S, G)}')
