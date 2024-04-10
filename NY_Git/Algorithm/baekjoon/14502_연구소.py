from collections import deque

def bfs(tlst):
    for i, j in tlst:
        arr[i][j] = 1


    q = deque()
    w = [[0] * M for _ in range(N)]
    cnt_zero = cnt - 3 # 남은 0의 개수 => 0의 개수 - 벽 3개

    # 선택된 3개의 벽을 설치하기
    for ti, tj in virus:
        q.append((ti, tj))
        w[ti][tj] = 1

    while q:
        r, c = q.popleft()

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < M and w[nr][nc] == 0 and arr[nr][nc] == 0:
                q.append((nr, nc))
                w[nr][nc] = 1
                cnt_zero -= 1 # 0의 개수에서 바이러스가 2로 번져서 1개씩 빼준다.

    # 다 끝나면 다시 벽 원상복구
    for i, j in tlst:
        arr[i][j] = 0

    return cnt_zero

# 3개의 벽을 설치하는 조합 (백트래킹)
def dfs(n, tlst):
    global ans

    if n == 3:
        ans = max(ans, bfs(tlst)) # 3개가 되면 바로 bfs 실행해서 최대값 return
        return

    # 3개의 벽을 설치하는 조합
    for i in range(cnt):
        if v[i] == 0:
            v[i] = 1
            dfs(n + 1, tlst + [lst[i]])
            v[i] = 0


# 입력
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

lst = [] # 0의 좌표를 담을 리스트
virus = [] # 2의 좌표를 담을 리스트
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0: # 0이면 lst에 append
            lst.append((i, j))
        if arr[i][j] == 2: # 2면 virus에 append
            virus.append((i, j))

cnt = len(lst) # 0의 개수
v = [0] * cnt # visited 배열 - 조합에 사용됨
ans = 0 # 최대값을 저장할 변수 생성

dfs(0, [])

print(ans)