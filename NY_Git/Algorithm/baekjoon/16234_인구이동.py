from collections import deque

def bfs(x, y, idx):
    # x, y와 연결된 연합 리스트
    united = []
    united.append((x, y))

    # 큐에 삽입
    q = deque()
    q.append((x, y))

    # level 배열 수정
    visited[x][y] = idx
    country_people = arr[x][y] # 국가의 사람 수
    country = 1 # 국가의 개수

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dr[d]
            ny = y + dc[d]

            # 범위 내에 있고 방문하지 않았다면
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if L <= abs(arr[nx][ny] - arr[x][y]) <= R: # 조건 범위 내라면
                    q.append((nx, ny)) # 큐에 삽입
                    visited[nx][ny] = idx # level 수정
                    country_people += arr[nx][ny] # 국가 사람 수에 더해줌
                    country += 1 # 국가 수 더해줌
                    united.append((nx, ny)) # 연합 배열에 추가

    # 추가된 연합국에 대해서 인구 나누기
    for i, j in united:
        arr[i][j] = country_people // country
    return country


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
answer = 0

# 모든 배열을 방문할 때까지 반복
while True:
    visited = [[-1] * N for _ in range(N)]
    idx = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                bfs(i, j, idx)
                idx += 1
    if idx == N*N:
        break
    answer += 1

print(answer)

