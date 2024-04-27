def dfs(start, target):  # 목적지까지 갈 수 있다면 0, 없다면 처음 마주치는 점유된 땅 번호

    pass


N, Q = map(int, input().split())  # N = 땅(노드의 개수) / Q = 오리 수

ducks = []
adj = [[] for _ in range(N // 2 + 1)]
visited = [0] * (N + 1)

# 완전이진트리 adj 만들기
for i in range(1, N // 2 + 1):
    adj[i].append(i * 2)
    if (i * 2 + 1) > N:
        break
    adj[i].append(i * 2 + 1)

for i in range(Q):
    ducks.append(int(input()))

for j in ducks:
    dfs(1, j)

print(adj)

1

