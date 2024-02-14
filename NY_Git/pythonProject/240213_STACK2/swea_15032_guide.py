# 미로

# DFS

N = 5
s = '1 2 1 3 3 4 4 5 4 2'

lst = list(map(int,s.split()))
G = [[] for _ in range(N+1)]

def dfs(stR, stC):
    ST = []
    visited = [[False] * N for _ in range(N+1)]       # 2차원 배열로 만들어야 한다.

    ST.append((stR, stC))
    visited[s] = True
    while ST:
        vR, vC = ST.pop()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newR =
            newC =
            if 갈 수 있는 곳인지 and not visited[newR][newC]:

                ST.append((newR, newC))
                visited[newR][newC] = True

    return 0

for i in range(0, len(lst), 2):
    v1 = lst[i]
    v2 = lst[i+1]
    G[v1].append(v2)
    G[v2].append(v1)

dfs(1)







T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    for row in range(N):
        for col in range(N):
            if arr[row][col] == 2:
                stR = row
                srC = col
                break

    for row in range(N):
        if arr[row].count(2):
            stC = arr[row].index(2)
            srT = row
            break
    print(stR, stC)

