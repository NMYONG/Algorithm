import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def dfs(start, last):
    global maxlast

    visited[start] = 1

    for i, j in tree[start]:
        if not visited[i]:
            maxlast = max(maxlast, last + j)
            dfs(i, last + j)


N = int(input())  # 방의 개수

tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    A, B, C = map(int, input().split())
    tree[A].append((B, C))
    tree[B].append((A, C))

maxlast = 0
visited = [0] * (N + 1)

dfs(1, 0)

print(maxlast)
