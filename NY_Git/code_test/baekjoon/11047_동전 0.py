import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []
cnt = 0
for _ in range(N):
    coins.append(int(input()))

coins = coins[::-1]

for idx in range(N):
    if K >= coins[idx]:
        cnt += K // coins[idx]
        K %= coins[idx]
    if K == 0: break

print(cnt)
