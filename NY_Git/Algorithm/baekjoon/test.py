from collections import deque

def bfs(row, col):
    q = deque()
    q.append((row, col))
    visited[row][col] = 1

    while q:
        r, c = q.popleft()

        dr = [-1, -1, -1, 0, 0, 1, 1, 1]
        dc = [-1, 0, 1, -1, 1, -1, 0, 1]

        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and arr[nr][nc] == 1:
                q.append((nr, nc))
                visited[nr][nc] = 1


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1

    print(cnt)