# # 고지식한  알고리즘
#
# def f(pat, txt, M, N):
#     for i in range(N-M+1):         # text에서 비교 시작 위치
#         for j in range(M):
#             if txt[i+j] != pat[j]: # 불일치면 다음 시작위치로
#                 break
#         else:                      # 패턴 매칭에 성공하면
#             return 1
#     return 0                       # 모든 위치에서 비교가 끝난 경우
#
# T = int(input())
# for tc in range(1, T+1):
#     pat = input()
#     txt = input()
#     M = len(pat)
#     N = len(txt)
#
#     print(f(pat, txt, M, N))



# 강사님 설명
# for
def find(p, t): # p가 t에 나타나면 t의 위치를 return, 없으면 -1 return
    M = len(p)
    N = len(t)

    for ti in range(N-M+1):
        for pi in range(M):
            if p[pi] != t[ti+pi]:
                break
        else: # break를 거치지 않고 반목문을 다 돌았을 경우
            return ti
    return -1

p = 'is'
t = 'This is a book'

print(find(p, t))


# while
def find(p, t): # p가 t에 나타나면 t의 위치를 return, 없으면 -1 return
    M = len(p)
    N = len(t)

    ti , pi = 0
    while ti < N and pi < M:
        if t[ti] == p[pi]:
            ti += 1
            pi += 1
        else:
            ti = ti - pi + 1
            pi = 0 # pi - pi
    if pi == M:
        return ti - pi
    else:
        return -1
