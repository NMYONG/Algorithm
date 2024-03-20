from collections import deque

# bfs => 마지막 깊이의 노드를 반환
def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        c = q.popleft()
        lst = []

        for n in adj[c]:
            if visited[n] == 0:
                visited[n] = visited[c] + 1
                q.append(n)
                lst.append(n)


T = 10
for tc in range(1, T+1):
    num, start = map(int, input().split())
    num_lst = list(map(int, input().split()))

    # 방문 리스트 생성
    visited = [0] * 101
    # 인접 리스트 생성
    adj = [[] for _ in range(100+1)]
    for i in range(0, num, 2):
        v1 = num_lst[i]
        v2 = num_lst[i+1]

        adj[v1].append(v2)

    bfs(start)

    lst = []
    v_max = max(visited)

    for i in range(len(visited)):
        if visited[i] == v_max:
            lst.append(i)
    print(f'#{tc} {max(lst)}')