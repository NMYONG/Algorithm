# 인접 행렬 DFS
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0]
]

visited = [0] * 5

def dfs(now):
    print(now, end=' ')

    for to in range(5):
        # 갈 수 없다면
        if graph[now][to] == 0:
            continue
        # 이미 방문 했다면
        if visited[to]:
            continue

        visited[to] = 1
        dfs(to)

visited[0] = 1
dfs(0)




# 인접 리스트 DFS
graph = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3]
]

visited = [0] * 5

def dfs(now):
    print(now)

    for to in graph[now]:
        if visited[to]:
            continue

        visited[to] = 1
        dfs(to)

visited[0] = 1
dfs(0)




# def dfs(c):
#     c.append(ans_dfs)
#     visited[c] = 1
#
#     for n in graph[c]:
#         if visited[n] == 0:
#             dfs(n)
