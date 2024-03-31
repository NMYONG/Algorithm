from collections import deque

def bfs(row, col, n, visited):
    q = deque()
    q.append((row, col))
    visited[row][col] = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dr[d]
            ny = y + dc[d]

            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] > n and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
max_v = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] > max_v:
            max_v = arr[i][j]

result = 0
for i in range(max_v):
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    for j in range(N):
        for k in range(N):
            if arr[j][k] > i  and visited[j][k] == 0:
                bfs(j, k, i, visited)
                cnt += 1

    if cnt > result:
        result = cnt

print(result)