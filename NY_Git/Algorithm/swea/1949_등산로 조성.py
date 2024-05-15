import sys, copy
sys.stdin = open('1949_등산로 조성.txt', 'r')


# def dfs(r, c, len, arr):
#     global max_len
#
#     visited[r][c] = 1  # 방문 표시
#     max_len = max(max_len, len)
#
#     for d in range(4):
#         nr = r + dr[d]
#         nc = c + dc[d]
#
#         if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] < arr[r][c]:
#             dfs(nr, nc, len + 1)
#
#     visited[r][c] = 0  # 백트래킹

def dfs(r, c, last, flag):
    global max_len

    visited[r][c] = 1
    max_len = max(max_len, last)

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]: # 범위 내에 있고 방문하지 않았다면
            if arr[nr][nc] >= arr[r][c]:
                for k in range(1, K+1): # 1부터 K까지 깎기
                    arr[nr][nc] -= k

            else:
                visited[nr][nc] = 1
                dfs(nr, nc, last+1, True)



T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    max_v = 0  # 최고점의 높이
    highest_lst = []  # 최고점의 좌표리스트

    # 최고 높이 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= max_v:
                max_v = arr[i][j]
    # 최고 높이 리스트에 넣어주기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_v:
                highest_lst.append((i, j))

    max_len = 0  # 등산로의 최대길이 변수 초기화
    for row, col in highest_lst:
        visited = [[0] * N for _ in range(N)]
        temp_arr = copy.deepcopy(arr) # 깊은복사한 arr에 대해서 dfs실행

        dfs(row, col, 1, True)

    print(max_len)
