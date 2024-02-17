# 미로의 거리

# 시작위치 구하기
def getStart(graph):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                start_r, start_c = i, j
                return start_r, start_c

def bfs(start_r, start_c):
    Q = []
    visited = [[0] * N for _ in range(N)]

    Q.append((start_r, start_c))
    visited[start_r][start_c] = 1

    while Q:
        vr, vc = Q.pop(0)

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r = vr + dr
            new_c = vc + dc

            if (0 <= new_r < N and 0 <= new_c < N) and graph[new_r][new_c] == 0 and not visited[new_r][new_c]:
                Q.append((new_r, new_c))
                visited[new_r][new_c] = visited[vr][vc] + 1

            elif (0 <= new_r < N and 0 <= new_c < N) and graph[new_r][new_c] == 3 and not visited[new_r][new_c]:
                return visited[vr][vc] - 1
    return 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]

    start_r, start_c = getStart(graph)
    result = bfs(start_r, start_c)

    print(f'#{tc} {result}')