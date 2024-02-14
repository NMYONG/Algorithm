# N = 4
# numbers = [11, 3, 7, 12]
# result = [0, 0, 0, 0]

# for i0 in [0, 1]:
#     result[0] = i0
#     for i1 in [0, 1]:
#         result[1] = i1
#         for i2 in [0, 1]:
#             result[2] = i2
#             for i3 in [0, 1]:
#                 result[3] = i3
#                 print((result))



# # 재귀함수 사용
# result = [-1] * N # 0부터 데이터가 들어가기 때문에 -1로 초기화
#
# def subset(k):
#     if k == N:
#         print(result, '=>', end='')
#         sumV = 0
#
#         for i in range(N):
#             if result[i]:
#                 sumV += numbers[i]
#         print(sumV)
#         return
#
#     for i in [0, 1]:
#         result[k] = i
#         subset(k+1)
#
# subset(0)



# 부분집합의 합
N = 10
result = [-1] * N
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9]

def subSum(k, curS):
    if k == N:


        sumV = 0
        for i in range(N):
            if result[i]:
                sum += numbers[i]
        if sumV == 10: # 부분집합의 합이 10인경우 출력
            print(result)
            for i in range(N):
                if result[i]:
                    print(numbers[i], end='')
            print()
        return

    for d in [0, 1]: # 없으면 0 있으면 1
        result[k] = d
        if d == 0:
            subSum(k+1)
        else:
            subSum(k+1)

subSum(0)



# 부분집합
N = 3
result = [-1] * N

# c 배열에 후보를 만들어서 개수를 return
def construct_candidates(k, c):
    c[0] = 0
    c[1] = 1
    c[2] = 2
    return 3 # 3개

def process_solution():
    print(result)

def recur_g(k):
    if k == N:
        process_solution()
        return

    c = [-1] * 100 # c 초기화
    nC = construct_candidates(k, c) # 구조화 하기 (결과 리스트의 length)
    for i in range(nC): # 호출하는 세로방향 depth
        result[k] = c[i]
        recur_g(k+1)

recur_g(0)