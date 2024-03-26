from collections import deque

# 배열의 합을 구하는 함수
def make_sum(arr):
    sum_arr = 0

    for i in range(N):
        for j in range(M):
            sum_arr += arr[i][j]
    return sum_arr

#
def bfs(row, col):
    # 배열에서 치즈를 만나면 return
    if arr[row][col] == 1:
        return

    # 모서리는 not_bubble 배열에 추가
    if row == 0 or row == N-1 or col == 0 or col == M-1:
        not_bubble.append((row, col))
        return

    # BFS 돌면서 테두리를 만나면 not_bubble 배열에 추가
    q = deque()
    q.append((row, col))
    visited = [[0] * M for _ in range(N)]
    visited[row][col] = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and not arr[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1
                if nr == 0 or nr == N - 1 or nc == 0 or nc == M - 1:
                    not_bubble.append((row, col))
                    return
    return not_bubble

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

# 단계
step = 0
sum_arr = make_sum(arr)
remain = [0]

while True:
    # 버블이 아닌 빈 공간
    not_bubble = []
    for i in range(N):
        for j in range(M):
            bfs(i, j)

    # not_bubble 배열의 원소에 대해서 4방향을 돌며 1이면 0으로 바꿔주고 cnt += 1
    for a, b in not_bubble:
        for d in range(4):
            na = a + dr[d]
            nb = b + dc[d]
            if 0 <= na < N and 0 <= nb < M and arr[na][nb]:
                arr[na][nb] = 0
    # 단계 +1
    step += 1
    sum_arr = make_sum(arr)
    remain.append(sum_arr)

    if not sum_arr: break

print(step)
print(remain[step-1])



# 공기방울 찾기(not_bubble 배열 생성, 0에 대해서 bfs(0, 0) 실행(4방향), 벽을 만나면 배열에 추가)
# 추가한 공기방울 순회하면서 4방향에 대해서 치즈를 만나면 0으로 바꿔줌 cnt + 1
# 종료 조건 : 원본 배열의 합이 0이 되는 시점