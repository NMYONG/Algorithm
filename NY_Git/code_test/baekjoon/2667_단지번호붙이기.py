from collections import deque

def bfs(row, col): # 단지의 아파트 개수를 return
    cnt = 1
    q = deque([])
    q.append((row, col))
    visited[i][j] = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d],

            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] == 1:
                q.append((nr, nc))
                visited[nr][nc] = 1
                cnt += 1

    return cnt

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

ans = []
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0: # 방문하지 않은 아파트 발견 시
            ans.append(bfs(i, j))

ans.sort()
print(len(ans), *ans, sep='\n')