'''
0 : 방
1 ~ 5 : CCTV
6 : 벽

cctv의 방향 0, 1, 2, 3 => 상, 하, 좌, 우

사각지대의 최소값 => 0의 최소값
'''

def dfs(n, lst):
    if n == 3:
        cctv_comb.append(lst[:])
        return

    visited = [0] * len(cctv)
    if i in range(len(cctv)):
        if visited[i] == 0:
            visited[i] = 1
            for d in range(4):
                cctv[i][2] = d
                dfs(n + 1, lst + [cctv][i])
            visited[i] = 0



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cctv = []
cctv_comb = []
for i in range(N):
    for j in range(M):
        if arr[i][j] in [1, 2, 3, 4, 5]:
            cctv.append([i, j, 0])

dfs(0, [])

print(cctv)
print(cctv_comb)