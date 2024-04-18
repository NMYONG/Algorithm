from collections import deque

def bfs(row, col):
    q = deque()

    q.append((i, j))
    visited[i][j] = 1

    while q:
        r, c = q.popleft()

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[X][Y] = 1

    visited = [[0] * M for _ in range(N)]
    answer = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                answer += 1

    print(answer)