# 삭제된 노드에 visited를 -1로 바꿔주는 함수
def delete(d):
    if visited[d] == [0]:
        return

    for c in adj[d]:
        visited[c] = 0
        dfs(c)

    visited[d] = 0

# 리프 노드의 개수를 찾는 함수
def dfs(start):
    global cnt

    if adj[start] == []:
        cnt += 1

    for c in adj[start]:
        if visited[c] != 0:
            dfs(c)

N = int(input())
numList = list(map(int, input().split()))
M = int(input())
adj = [[] for _ in range(N)]
visited = [[1] for _ in range(N)]

cnt = 0 # 리프노드의 개수를 count

# adj 배열 만들기(0번 노드부터 시작한다.)
for i in range(len(numList)): # i = 0, 1, 2, 3, 4
    if numList[i] == -1:
        continue
    else:
        adj[numList[i]].append(i)

delete(M)
dfs(0)


print(adj)
print(visited)
print(cnt)