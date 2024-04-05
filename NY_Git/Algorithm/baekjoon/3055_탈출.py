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


def dfs():
    while q:
        r, c = q.popleft()
        visited[r][c] = 0

        if maps[Dr][Dc] == 'S':  # 고슴도치가 굴에 도착하면
            return visited[Dr][Dc] # 거리 반환

        for d in range(4): # 고슴도치의 자리에서 4방향 탐색
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < R and 0 <= nc < C: # 범위 내에 있다면
                # 현재 위치가 S이고 이동할 자리가 .이거나 D이면 (고슴도치 이동)
                if (maps[nr][nc] == '.' or maps[nr][nc] == 'D') and maps[r][c] == 'S':
                    visited[nr][nc] = visited[r][c] + 1
                    maps[nr][nc] = 'S'
                    q.append((nr, nc))
                # 현재 위치가 *이고 이동할 자리가 .이거나 S이면 (물 이동)
                elif (maps[nr][nc] == '.' or maps[nr][nc] == 'S') and maps[r][c] == '*':
                    maps[nr][nc] = '*'
                    q.append((nr, nc))


R, C = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(R)]

q = deque()
visited = [[-1] * C for _ in range(R)] # 거리를 계산할 2중배열 만들기
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for r in range(R):
    for c in range(C):
        if maps[r][c] == 'S':
            q.append((r, c))
        if maps[r][c] == 'D':
            Dr, Dc = r, c

for r in range(R):
    for c in range(C):
        if maps[r][c] == '*':
            q.append((r, c))


# https://yunchan97.tistory.com/35