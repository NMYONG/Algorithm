# swea_4881
def f(i, k, s):
    global cnt
    global min_v
    cnt += 1                                # 함수 실행 횟수 증가
    if i == k:
        # s = 0                               # 선택한 원소의 합
        # for j in range(k):                  # j행에 대해
        #     s += arr[j][P[j]]               # j행에서 P[j]열을 고른 경우의 합 구하기
        if min_v > s:
            min_v = s
    elif s >= min_v:                        # 백트래킹: 현재까지의 합이 이미 최솟값을 초과하면 더 이상 진행할 필요가 없음
        return
    else:
        for j in range(i, k):               # P[i] 자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i]         # P[i] <-> P[j]
            f(i+1, k, s+arr[i][P[i]])
            P[i], P[j] = P[j], P[i]         # 교환 전으로 복구

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
P = [i for i in range(N)]
min_v = float('inf')                        # 최솟값을 비교할 때 초기값을 무한대로 설정
cnt = 0

f(0, N, 0)
print(min_v, cnt)
