# 고지식한  알고리즘

def f(pat, txt, M, N):
    for i in range(N-M+1):         # text에서 비교 시작 위치
        for j in range(M):
            if txt[i+j] != pat[j]: # 불일치면 다음 시작위치로
                break
        else:                      # 패턴 매칭에 성공하면
            return 1
    return 0                       # 모든 위치에서 비교가 끝난 경우

T = int(input())
for tc in range(1, T+1):
    pat = input()
    txt = input()
    M = len(pat)
    N = len(txt)

    print(f(pat, txt, M, N))