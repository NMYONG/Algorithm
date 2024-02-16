def getStart(graph):
    for i in range(16):
        for j in range(16):
            if graph[i][j] == 2:
                start_r, start_c = i, j
                return start_r, start_c

def bfs(start_r, start_c):
    Q = []
    visited = [[False] * 16 for _ in range(16)]

    Q.append((start_r, start_c))
    visited[start_r][start_c] = True

    while Q:
        vr, vc = Q.pop(0)

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r = vr + dr
            new_c = vc + dc

            if 0 <= new_r < 16 and 0 <= new_c < 16:
                if graph[new_r][new_c] == 3:
                    return 1
                if graph[new_r][new_c] != 1 and not visited[new_r][new_c]:
                    Q.append((new_r, new_c))
                    visited[new_r][new_c] = True
    return 0


for _ in range(2):
    tc = int(input())
    graph = [list(map(int, input())) for _ in range(16)]

    start_r, start_c = getStart(graph)
    result = bfs(start_r, start_c)

    print(f'#{tc}')
    print(result)