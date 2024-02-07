def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M+1)

    # preprocessing
    j = 0 # 일치한 개수 == 비교할 패턴 위치
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j          # p[i] 이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j
    # search
    i = 0 # 비교할 텍스트 위치
    j = 0 # 비교할 패턴 위치
    while i < N and j <= M:
        if j == -1 or t[i] == p[j]: # 첫 글자가 불일치했거나, 일치하면
            i += 1
            j += 1
        else:       # 불일치
            j = lps[j]
        if j == M: # 패턴을 찾을 경우
            print(i-M)
            j = lps[j] # 계속해서 검색을 위해 초기화


# 강사님 설명
def make(p):
    M = len(p)
    j = 0
    for i in range(1, M):
        lps[i] = j
        if p[i] == p[j]:
            j += 1
        else:
            j = 0

def find(p, t):
    N = len(t)
    M = len(p)
    ti = pi = 0

    while ti < N and pi < M:
        if pi == -1 or t[ti] == p [pi]:
            ti += 1
            pi += 1
        else:
            pi = lps[pi]
    if pi == M:
        return ti - pi
    else:
        return -1


t = 'zzabcdabcefgg'
p = 'abcdabcef'


lps = [-1] * len(p)
