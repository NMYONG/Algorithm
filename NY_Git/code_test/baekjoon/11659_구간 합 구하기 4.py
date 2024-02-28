import sys
input = sys.stdin.readline
#
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
#
# cumul_sum = [0] * (N+1)
# for i in range(1, N+1):
#     cumul_sum[i] = cumul_sum[i-1] + arr[i-1]
#
# for _ in range(M):
#     start, end = map(int, input().split())
#     result = cumul_sum[end] - cumul_sum[start - 1]
#
#     print(result)


N, M = map(int, input().split())
arr = list(map(int, input().split()))

culm_sum = [0] * (N+1)
for i in range(1, N+1):
    culm_sum[i] = culm_sum[i-1] + arr[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    result = culm_sum[j] - culm_sum[i-1]

