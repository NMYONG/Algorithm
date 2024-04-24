import sys
from collections import deque
input = sys.stdin.readline

def bfs(row, col):
    cnt = 0
    q = deque()
    q.append((row, col))
    visited[row][col] = 1
    cnt += 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            new_r = r + dr[d]
            new_c = c + dc[d]

            if 0 <= new_r < n and 0 <= new_c < m and arr[new_r][new_c] == 1 and visited[new_r][new_c] == 0:
                visited[new_r][new_c] = 1
                q.append((new_r, new_c))
                cnt += 1

    ans_bfs.append(cnt)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 변수 초기화
ans_bfs = []
visited = [[0] * m for i in range(n)]
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
is_zero = 0

for i in range(n):
    for j in range(m):
        is_zero += arr[i][j]

if not is_zero:
    print(0)
    print(0)
else:
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
    print(len(ans_bfs))
    print(max(ans_bfs))

    