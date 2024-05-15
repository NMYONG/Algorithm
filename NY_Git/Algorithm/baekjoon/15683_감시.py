'''
0 : 방
1 ~ 5 : CCTV
6 : 벽

cctv의 방향 0, 1, 2, 3 => 상, 하, 좌, 우

사각지대의 최소값 => 0의 최소값
'''

# def dfs(n, lst):
#     if n == 3:
#         cctv_comb.append(lst[:])
#         return
#
#     visited = [0] * len(cctv)
#     if i in range(len(cctv)):
#         if visited[i] == 0:
#             visited[i] = 1
#             for d in range(4):
#                 cctv[i][2] = d
#                 dfs(n + 1, lst + [cctv][i])
#             visited[i] = 0
#
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# cctv = []
# cctv_comb = []
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] in [1, 2, 3, 4, 5]:
#             cctv.append([i, j, 0])
#
# dfs(0, [])
#
# print(cctv)
# print(cctv_comb)

# 상, 우, 하, 좌 방향
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
direction = [[], [1], [1, 3], [0, 1], [0, 1, 3], [0, 1, 2, 3]]


def cal(tempList):
    visited = [[0] * (M + 2) for _ in range(N + 2)]

    # 모든 CCTV에 대해서 좌표, rot, type 설정
    for i in range(cctvCount):
        row, col = CCTV[i]  # 1~N, 1~M
        rot = tempList[i]  # 0 ~ 3
        type = arr[row][col]  # 1 ~ 5

        for d in direction[type]:
            d = (d + rot) % 4
            cr, cc = row, col
            while True:
                cr, cc = cr + dr[d], cc+dc[d]
                if arr[cr][cc] == 6: # 벽을 만나면
                    break
                visited[cr][cc] = 1

    cnt = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if arr[i][j] == 0 and visited[i][j] == 0:
                cnt += 1
    return cnt


def dfs(n, tempList):
    global ans

    if n == cctvCount:  # 모든 CCTV의 방향이 정해졌다면
        ans = min(ans, cal(tempList))
        return

    # 0, 90, 180, 270 회전
    dfs(n + 1, tempList + [0])
    dfs(n + 1, tempList + [1])
    dfs(n + 1, tempList + [2])
    dfs(n + 1, tempList + [3])


N, M = map(int, input().split())
# 벽(6)으로 테두리 둘러주기
arr = [[6] * (M + 2)] + [[6] + list(map(int, input().split())) + [6] for _ in range(N)] + [[6] * (M + 2)]
# CCTV 좌표 저장하기
CCTV = []
for i in range(1, N + 1):  # 6으로 막았으니 범위 수정
    for j in range(1, M + 1):
        if 1 <= arr[i][j] <= 5:  # CCTV라면
            CCTV.append((i, j))

cctvCount = len(CCTV)
ans = float('inf')  # 최소값이니까 무한대로 초기화
dfs(0, [])
print(ans)
