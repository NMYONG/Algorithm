import sys
input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

print(adj)

for i in range(2, N+1):
    print(adj[i][0])