import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N + 1)]
parent = [0] * (N + 1) # 각 노드의 부모를 기록하는 배열
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# print(adj)

def dfs(v):
    for i in adj[v]:
        if not parent[i]: # 부모를 찾지 못했다면
            parent[i] = v # v와 연결되어 있는데 부모 배열이 0이다? => v가 부모다.
            dfs(i)

dfs(1)

for j in range(2, len(parent)):
    print(parent[j])