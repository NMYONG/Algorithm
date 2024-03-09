from collections import deque
def bfs():
    while q:
        r, c = q.popleft()

        # delta 4방향 탐색
        for d in range(4):
            new_r = r + dr[d]
            new_c = c + dc[d]

            # 배열 안에 새로운 r, c가 있고 그 값이 0이라면(익지 않았다면)
            if 0 <= new_r < N and 0 <= new_c < M and container[new_r][new_c] == 0:
                container[new_r][new_c] = container[r][c] + 1 # 탐색하면서 1씩 더해줌
                q.append([new_r, new_c])

M, N = map(int, input().split())
container = [list(map(int, input().split())) for _ in range(N)]
q = deque([])
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
day = 0

# 시작 row, col 찾아서 큐에 넣기
for row in range(N):
    for col in range(M):
        if container[row][col] == 1:
            q.append([row, col])

bfs()
for i in container:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    day = max(day, max(i))
print(day-1)

# visited 배열 쓸 필요 없는 이유 : 0이면 이동, 나머지는 이동x
# 어려운 점 : 마지막 조건