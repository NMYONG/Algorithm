'''
R행 C열
비어있는 곳 .
물 차있는 곳 *
돌 X
비버의 돌 D
고슴도치 위치 S
'''
import sys
from collections import deque
input = sys.stdin.readline

def dochi_bfs(row, col):
    q = deque()
    q.append((row, col))
    visited[row][col] = 1 # 나중에 1 빼주기

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1


N, M = map(int, input().split())
maps = [list(input()) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[0] * M for _ in range(N)]

gool_r = 0
gool_c = 0
for i in range(N):
    for j in range(M):
        if maps[i][j] == 'D':
            gool_r = i
            gool_c = j

dochi_r = 0
dochi_c = 0
for i in range(N):
    for j in range(M):
        if maps[i][j] == 'S':
            dochi_r = i
            dochi_c = j

dochi_bfs(dochi_r, dochi_c)

print(visited[gool_r][gool_c])