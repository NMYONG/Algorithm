from collections import deque


# 현재 좌표에서 타겟 좌표까지 최단거리를 반환하는 함수
def findMinRnage(current, target, current_size):
    q = deque()
    visited = [[0] * N for _ in range(N)]
    minRnage = float('inf')

    q.append(current)
    visited[current[0]][current[1]] = 1

    while q:
        r, c = q.popleft()

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] <= current_size:
                visited[nr][nc] = 1
                q.append((nr, nc))
                if arr[nr][nc] == arr[target[0]][target[1]]:
                    minRnage = min(minRnage, visited[nr][nc])
                    return minRnage
    return -1

# 현재 map과 상어의 크기에 대해서 먹을 수 있는 물고기의 위치 반환
def search(arr, current_size):
    canEatLst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= current_size:
                canEatLst.append((i, j))

    for i in canEatLst:
        findMinRnage((shark[0], shark[1]), i, shark[2])


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 상어의 위치 찾기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            shark = (i, j, 2)

