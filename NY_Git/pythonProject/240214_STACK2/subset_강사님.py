# 부분집합
def subSet(k):
    if k == N:
        print(check)
        sum_v = 0
        for i in range(N):
            if check[i]:
                sum_v += numbers[i]
                # print(numbers[i], end=' ')
        print(sum_v)
        return

    for i in [0, 1]:
        check[k] = i
        subSet(k+1)

N = 3
numbers = [10, 30, 20]
check = [-1] * N

subSet(0)



# # 부분집합_백트래킹
# def subSet(k):
#     if k == N:
#         sum_v = 0
#         for i in range(N):
#             if check[i]:
#                 sum_v += numbers[i]
#         if sum_v <= 50:  # 백트래킹: 합이 50 이하일 때만 출력
#             print(check)
#             print(sum_v)
#         return
#
#     for i in [0, 1]:
#         check[k] = i
#         subSet(k+1)
#
# N = 3
# numbers = [10, 30, 20]
# check = [-1] * N
#
# subSet(0)
