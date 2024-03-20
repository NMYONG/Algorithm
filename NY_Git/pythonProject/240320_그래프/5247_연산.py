from collections import deque

def bfs(s):
    q = deque()
    q.append(s)

    visited = [0] * 1000001
    visited[s] = 1

    while q:
        c = q.popleft()
        # 정답과 같으면
        if c == M:
            return visited[c] - 1 # visited[s] = 1에서는 연산 한 것이 아니므로
        # 정답이 아니면 네가지 연산에 대해서
        for n in ((c - 1), (c + 1), (c * 2), (c - 10)):
            if 1 <= n <= 1000000 and visited[n] == 0:
                visited[n] = visited[c] + 1 # 이전 연산 횟수에서 1 더해줌
            q.append(n)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    ans = bfs(N)
    print(f'#{tc} {ans}')
