def dfs(s):
    visited[s] = 1

    for n in adj[s]:
        if visited[n] == 1:
            continue
        dfs(n)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    apply = list(map(int, input().split()))

    # 인접 리스트 생성
    adj = [[] for _ in range(N + 1)]
    for i in range(0, len(apply), 2):
        v1 = apply[i]
        v2 = apply[i + 1]
        adj[v1].append(v2)
        adj[v2].append(v1)

    visited = [0 for _ in range(N + 1)]
    cnt = 0

    # 모든 노드에 대해 dfs 실행
    for i in range(1, N + 1):
        if visited[i]:
            continue
        dfs(i)
        cnt += 1

    print(f'#{tc} {cnt}')
