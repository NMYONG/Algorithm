from collections import deque

def bfs(si, sj):
    q = deque()
    visited = [[0] * N for _ in range(N)]
    eatableList = []

    q.append((si, sj))
    visited[si][sj] = 1
    distance = 0

    while q:
        r, c = q.popleft()

        if distance == visited[r][c]:
            return eatableList, distance - 1

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and sharkSize >= arr[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                if sharkSize > arr[nr][nc] > 0:
                    eatableList.append((nr, nc))
                    distance = visited[nr][nc]

    return eatableList, distance - 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 상어의 위치 찾기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            ci, cj = i, j
            arr[i][j] = 0 # 이동할거니까 위치 0으로 만들기

sharkSize = 2
cnt = 0 # 물고기를 먹은 회수
ans = 0 # 총 이동 거리

while True:
    eatableList, dist = bfs(ci, cj)
    if len(eatableList) == 0: # 먹을 수 있는 물고기가 없으면 종료
        break
    eatableList.sort(key=lambda x: (x[0], x[1])) # 정렬 row, col 순으로
    ci, cj = eatableList[0] # 상어가 이동할 위치 (먹을 물고기의 위치)
    arr[ci][cj] = 0
    cnt += 1 # 먹은 물고기 개수 증가
    ans += dist
    if sharkSize == cnt: # 상어크기만큼 물고기를 먹었으면
        sharkSize += 1
        cnt = 0

print(ans)