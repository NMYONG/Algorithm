import sys
from collections import deque
input = sys.stdin.readline


# bfs
def bfs(row, col):
    q = deque()
    q.append((row, col))
    # visited[row][col] = 1

    while q:
        r, c = q.popleft()
        for d in range(8):
            new_r = r + dr[d]
            new_c = c + dc[d]

            if 0 <= new_r < N and 0 <= new_c <M and arr[new_r][new_c] == 1:
                q.append((new_r, new_c))
                arr[new_r][new_c] = 0


# 입력
while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0: break
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    # visited = [[0] * M for _ in range(M)]

    for row in range(N):
        for col in range(M):
            if arr[row][col] == 1 :
                bfs(row, col)
                cnt += 1

    print(cnt)