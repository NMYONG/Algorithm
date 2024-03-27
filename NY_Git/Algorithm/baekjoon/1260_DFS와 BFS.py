def dfs(c):
    ans_dfs.append(c)   # 방문한 노드 추가
    visited[c] = 1      # 방문 표시

    for n in adj[c]:    # 방문한 노드에 대해서 연결된 노드들을 검사
        if visited[n] == 0: # 방문하지 않았으면
            dfs(n)

def bfs(s):
    q = []              # 큐 생성
    q.append(s)

    ans_bfs.append(s)
    visited[s] = 1      # 방문 표시

    while q:
        c = q.pop(0)
        for n in adj[c]:
            if visited[n] == 0: # 방문하지 않은 노드라면 q에 삽입
                q.append(n)
                ans_bfs.append(n)
                visited[n] = 1

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)  # 양방향

for i in range(1, N+1): # 오름차순 정렬
    adj[i].sort()

visited = [0] * (N + 1)
ans_dfs = []
dfs(V)

visited = [0] * (N + 1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)