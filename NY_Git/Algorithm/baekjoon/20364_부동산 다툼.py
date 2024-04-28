def dfs(start, target):  # 목적지까지 갈 수 있다면 0, 없다면 처음 마주치는 점유된 땅 번호
    global canVisitable

    if start == target:
        visited[start] = start
        return

    for c in adj[start]:
        if not visited[c]: # 연결된 땅에 점유한 오리가 없으면
            dfs(c, target)

        else: # 점유한 오리가 있으면
            canVisitable = visited[c]
            return


N, Q = map(int, input().split())  # N = 땅(노드의 개수) / Q = 오리 수

ducks = []
adj = [[] for _ in range(N+1)]
visited = [0] * (N + 1)

# 완전이진트리 adj 만들기
for i in range(1, N // 2 + 1):
    adj[i].append(i * 2)
    if (i * 2 + 1) > N:
        break
    adj[i].append(i * 2 + 1)

# 오리가 가고싶은 땅 저장하기
for i in range(Q):
    ducks.append(int(input()))

print(adj)
print(visited)

for j in ducks:
    canVisitable = 0
    dfs(1, j)
    print(canVisitable)



