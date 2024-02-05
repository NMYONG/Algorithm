T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     num = input()
#
#     current_cnt = 1
#     max_cnt = 1
#
#     for i in range(N-1):
#         if num[i] == '1' and num[i+1] == '1':
#             current_cnt += 1
#             max_cnt = max(max_cnt, current_cnt)
#         else:
#             current_cnt = 1
#
#
# print(f'#{tc} {max_cnt}')



for tc in range(1, T+1):
    N = int(input())
    S = input()

    cnt = 0
    maxV = 0

    for c in S:
        if c == '1':
            cnt += 1
        else:
            if maxV < cnt:
                maxV = cnt
            cnt = 0
    if maxV < cnt:
        maxV = cnt

    print(f'#{tc} {maxV}')