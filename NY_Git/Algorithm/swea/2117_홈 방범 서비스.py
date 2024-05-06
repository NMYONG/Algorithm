import sys

sys.stdin = open("2117_홈 방범 서비스.txt", "r")


# 완전탐색으로 풀이
def solve():
    ans = 0
    for si in range(N):
        for sj in range(N):
            for k in range(1, 2 * N):
                cnt = 0
                for i in range(si - k + 1, si + k):
                    for j in range(sj - k + 1 + abs(i - si), sj + k - abs(i - si)):
                        # 범위내이고 집인경우
                        if 0 <= i < N and 0 <= j < N and arr[i][j]:
                            cnt += 1
                cost = k * k + (k - 1) * (k - 1)
                if cost <= cnt * M and ans < cnt:
                    ans = cnt

    return ans


# 완전탐색 개선하기
cost = [(k * k + (k - 1) * (k - 1)) for k in range(40)]


def solve1():
    ans = 0
    for si in range(N):
        for sj in range(N):
            for k in range(1, 2 * N):
                cnt = 0
                for i in range(si - k + 1, si + k):
                    for j in range(sj - k + 1 + abs(i - si), sj + k - abs(i - si)):
                        # 범위내이고 집인경우
                        if 0 <= i < N and 0 <= j < N and arr[i][j]:
                            cnt += 1
                # cost = k*k + (k-1)*(k-1)
                if cost[k] <= cnt * M and ans < cnt:
                    ans = cnt

    return ans


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = solve1()

    print(f'#{tc} {ans}')
