# from collections import deque
#
#
# def bfs(wall):
#     global safety_zone
#
#     while q:
#         r, c = q.popleft()
#
#         for d in range(4):
#             nr = r + dr[d]
#             nc = c + dc[d]
#
#             if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
#                 # 벽을 만드는 경우
#                 bfs(wall-1)
#                 # 벽을 만들지 않는 경우
#                 bfs(wall)
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# safety_zone = 0
# wall = 3
# q = deque()
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# # 바이러스 찾기
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 2:
#             q.append((i, j))
#
# bfs(3)




# 조합 풀이

