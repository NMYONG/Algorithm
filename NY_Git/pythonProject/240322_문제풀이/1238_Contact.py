def bfs(start):
    q = [start]
    visited = [0] * (101)
    visited[start] = 1

    # 가장 깊은 depth의 가장 큰 수
    max_number = start
    # 가장 깊은 depth 저장
    max_depth = 1

    while q:
        now = q.pop(0)

        for to in graph[now]:
            if visited[to]:
                continue

            visited[to] = visited[now] + 1
            # depth가 더 깊어짐 => max_number 초기화
            # depth는 같은데 max_number 커짐 => 초기화
            if max_depth < visited[to] or (max_depth == visited[to] and max_number < to):
                max_depth = visited[to]
                max_number = to

            q.append(to)

    return max_number


for tc in range(1):
    N, start = map(int, input().split())
    input_graph = list(map(int, input().split()))
    # 인접 리스트
    graph = [[] for _ in range(101)]
    for i in range(0, N, 2):
        s = input_graph[i]
        e = input_graph[i + 1]
        graph[s].append(s)

    r = bfs(0)
    print(f'{tc} {r}')