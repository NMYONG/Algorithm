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

# 도치가 움직일 수 있는 경로
def bfs(dochi):
    q = deque
    q.append(dochi)



N, M = map(int, input().split())
maps = [list(input()) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 물, 굴, 도치 좌표 구하기
mool_r, mool_c = 0, 0
gool_r, gool_c = 0, 0
dochi_r, dochi_c = 0, 0

for i in range(N):
    for j in range(M):
        if maps[i][j] == '*': # 물이면
            mool_r, mool_c = i, j
        if maps[i][j] == 'D':
            gool_r, gool_c = i, j
        if maps[i][j] == 'S':
            dochi_r, dochi_c = i, j

# 물과 도치가 같이 움직여야 하니까 둘 다 BFS 돌리자