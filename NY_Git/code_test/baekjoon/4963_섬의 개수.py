from collections import deque

dr, dc = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
cnt = 0

# bfs
def bfs(r, c):
    q = deque()
    q.append((r, c))

    while q:


# 입력
while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0: break
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * M for _ in range(M)]

    for row in range(N):
        for col in range(M):
            if arr[row][col] == 1 and visited[row][col] == 0:
                for d in range(8):
                    new_r = row + dr[d]
                    new_c = col + dc[d]

