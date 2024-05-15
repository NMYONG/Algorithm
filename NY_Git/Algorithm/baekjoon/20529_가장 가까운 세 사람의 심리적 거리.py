# 1. 세 명만 고르는 조합을 구하는 함수
def makeCombination(n, lst):
    if n == 3:
        combList.append(lst)
        return

    currMbti = ''
    for i in range(len(MBTI)):
        if not visited[i] and currMbti != MBTI[i]:
            visited[i] = 1
            makeCombination(n + 1, lst + [MBTI[i]])
            currMbti = MBTI[i]
            visited[i] = 0

# 2. 세 명의 심리적 거리를 구하는 함수
def cal(lst):
    cnt = 0
    # 첫번째, 두번째 비교
    for i in range(4): # i = 0, 1, 2, 4
        if lst[0][i] != lst[1][i]:
            cnt += 1
    # 첫번쨰, 세번쨰 비교
    for i in range(4): # i = 0, 1, 2, 4
        if lst[0][i] != lst[2][i]:
            cnt += 1
    # 두번쨰, 세번쨰 비교
    for i in range(4):  # i = 0, 1, 2, 4
        if lst[1][i] != lst[2][i]:
            cnt += 1
    return cnt


T = int(input())
for _ in range(T):
    N = int(input())
    MBTI = list(input().split())

    # N이 32 초과이면 답은 0이다.
    if N > 32:
        print(0)
        continue

    combList = []
    visited = [0] * len(MBTI)
    minDist = float('inf')

    makeCombination(0, [])
    # print(len(combList))
    # print(combList)

    for comb in combList:
        dist = cal(comb)
        if minDist > dist:
            minDist = dist

    print(minDist)

