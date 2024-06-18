import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MEMO = {}

for n in range(N):
    key, value = input().split()
    MEMO[key] = value

for m in range(M):
    key = input().strip()
    print(MEMO[key])