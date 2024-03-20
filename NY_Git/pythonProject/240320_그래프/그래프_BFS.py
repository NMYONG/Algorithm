# 인접 행렬 BFS
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0]
]


def bfs(start):
    visited = [0] * 5

    # 시작 노드를 큐에 추가, 방문 표시
    queue = [start]
    visited[start] = 1

    while queue:
        now = queue.pop(0)
        print(now, end=' ')

        for to in range(5):  # 인접 행렬이기 때문에 길이만큼 반복
            if graph[now][to] == 0:
                continue

            if visited[to]:
                continue

            visited[to] = 1
            queue.append(to)

bfs(0)

# 인접 리스트
graph = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3]
]







# def bfs(s):
#     q = []
#     q.append(s)
#
#     ans_bfs.append(s)
#     visited[s] = 1
#
#     while q:
#         c = pop(0)
#
#         for n in graph[c]:
#             if visited[n] == 0:
#                 ans_bfs.append(n)
#                 visited[n] = 1
#                 q.append(n)
