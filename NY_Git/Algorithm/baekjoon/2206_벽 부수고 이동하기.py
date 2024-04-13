# from collections import deque
#
#
# def bfs(row, col):
#     global min_distance
#
#     q = deque()
#     q.append((row, col))
#
#     flag = 0  # 벽을 부셨으면 1
#
#     visited = [[0] * M for _ in range(N)]
#     visited[row][col] = 1
#
#     while q:
#         r, c = q.popleft()
#
#         dr = [-1, 1, 0, 0]
#         dc = [0, 0, -1, 1]
#
#         for d in range(4):
#             nr = r + dr[d]
#             nc = c + dc[d]
#
#             if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc] == 0:
#                 q.append((nr, nc))
#                 visited[nr][nc] = visited[r][c] + 1
#
#     min_distance = min(min_distance, visited[N-1][M-1])
#
#
# N, M = map(int, input().split())
# arr = [input() for _ in range(N)]
#
# min_distance = float('inf')
#
# bfs(0, 0)
