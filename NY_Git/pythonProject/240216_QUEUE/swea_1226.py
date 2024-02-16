# 미로
def bfs(stR, stC):
    Q = []
    visited = [[False] * N for _ in range(N)]

    Q.append((stR, stC))
    visited[stR][stC] = True

    while Q:
        vR, vC = Q.pop(0)

        # 델타 활용해서 연결 지점 구하기
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            wR = vR + dr
            wC = vC + dc

            # 연결지점 조건
            if 0 <= wR < N and 0 <= wC < N: # 벽을 지났을 경우
                if arr[wR][wC] == 3: # Goal 도착
                    return 1
                if arr[wR][wC] != 1 and not visited[wR][wC]:  # 벽이 아니고 방문하지 않았으면
                    Q.append((wR, wC))
                    visited[wR][wC] = True
    return 0


for _ in range(1, 11):
    tc = int(input())
    N = 16
    arr = [list(map(int, input())) for _ in range(N)]

    # 시작지점 구하기
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 2:
                stR = row
                stC = col
                break
    # # 시작지점 구하기
    # for row in range(N):
    #     if arr[row].count(2):
    #         stC = arr[row].index(2)
    #         break
    # stR = row


    print(f'#{tc}')
    print(bfs(stR, stC))







#
#
# # 몇 번 만에 방문했는지?
# # 미로
# def bfs(stR, stC):
#     Q = []
#     visited = [[False] * N for _ in range(N)]
#
#     Q.append((stR, stC))
#     visited[stR][stC] = True
#
#     while Q:
#         vR, vC = Q.pop(0)
#
#         # 델타 활용해서 연결 지점 구하기
#         for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             wR = vR + dr
#             wC = vC + dc
#
#             # 연결지점 조건
#             if 0 <= wR < N and 0 <= wC < N:
#                 if arr[wR][wC] == 3:
#                     return visited[vR][vC] + 1
#
#                 if arr[wR][wC] != 1 and not visited[wR][wC]:  # 벽이 아니고 방문하지 않았으면
#                     Q.append((wR, wC))
#                     visited[wR][wC] = visited[vR][vC] + 1
#
#     return 0
#
#
# for _ in range(1, 11):
#     tc = int(input())
#     N = 16
#     arr = [list(map(int, input())) for _ in range(N)]
#
#     ## 시작지점 구하기
#     # for row in range(N):
#     #     for col in range(N):
#     #         if arr[row][col] == 2:
#     #             srR = row
#     #             stC = col
#     #             break
#     # 시작지점 구하기
#     for row in range(N):
#         if arr[row].count(2):
#             stC = arr[row].index(2)
#             break
#     stR = row
#
#
#     print(f'#{tc}')
#     print(bfs(stR, stC))