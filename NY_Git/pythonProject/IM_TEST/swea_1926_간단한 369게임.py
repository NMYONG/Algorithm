# N = int(input())
#
# for i in range(1, N + 1):
#     cnt = 0
#     num = str(i)
#     tmp = ['3', '6', '9']
#     for j in range(len(tmp)):
#         for k in range(len(num)):
#             if num[k] == tmp[j]:
#                 cnt += 1
#     if cnt > 0:
#         print('-' * cnt, end=' ')
#     else:
#         print(i, end=' ')
# print()
#
#
# # 인자로 받은 num에 각자리에 3,6,9에 해당하는 숫자가 몇 개인지 반환
# def check(num):
#     cnt = 0
#
#     while num > 0:
#         remain = num % 10
#         if remain in [3, 6, 9]:
#             cnt += 1
#         num //= 10
#     return cnt
#
#
# N = int(input())
#
# for i in range(1, N + 1):
#     cnt = check(i)
#     if cnt > 0:
#         print('-' * cnt, end=' ')
#     else:
#         print(i, end=' ')
# print()

# 내 풀이
N = int(input())

for i in range(1, N + 1):
    cnt = 0
    tmp = ['3', '6', '9']
    for j in str(i):
        if j in tmp:
            cnt += 1
    if cnt > 0:
        print('-' * cnt, end=' ')
    else:
        print(i, end=' ')
