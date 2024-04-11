N, M = map(int, input().split())
# 벽(6)으로 가장자리를 막는다.
arr = [[6]*(M+2) + [[6] + list(map(int, input().split())) + [6]] for _ in range(N)]

