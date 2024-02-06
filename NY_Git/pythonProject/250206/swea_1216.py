# import sys
# sys.stdin = open('swea_1216.txt', 'r')
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     arr = [list(input()) for _ in range(100)]
#
#     for M in range(1, 101):
#         reps = 100 - M + 1
#         max_len = []
#
#         # 행에 대해
#         for i in range(100):
#             for j in range(reps):
#                 forward_lst_row = arr[i][j:M + j]
#                 reverse_lst_row = forward_lst_row[::-1]
#
#                 if forward_lst_row == reverse_lst_row:
#                     answer = ''.join(forward_lst_row)
#                     try:
#                         max_len.append(len(forward_lst_row))
#                     except ValueError:
#                         pass
#
#         # 열에 대해
#         for i in range(100):
#             forward_lst_col = []
#             for j in range(reps):
#                 forward_lst_col2 = []
#                 for l in range(M):
#                     forward_lst_col2.append(arr[j + l][i])
#                 forward_lst_col.append(''.join(forward_lst_col2))
#
#             for k in range(len(forward_lst_col)):
#                 if forward_lst_col[k] == forward_lst_col[k][::-1]:
#                     answer = ''.join(forward_lst_col[k])
#                     try:
#                         max_len.append(len(forward_lst_col))
#                     except ValueError:
#                         pass
#
#     print(f'#{tc} {max(max_len)}')



import sys
sys.stdin = open('swea_1216.txt', 'r')


for tc in range(1,11):
    T = int(input())
    arr = [list(input()) for _ in range(100)]

    max_len = []

    # 행에 대해
    for i in range(100):
        for M in range(1, 101):
            reps = 100 - M + 1
            for j in range(reps):
                forward_lst_row = arr[i][j:M + j]
                reverse_lst_row = forward_lst_row[::-1]

                if forward_lst_row == reverse_lst_row:
                    max_len.append(len(forward_lst_row))

    # 열에 대해
    for i in range(100):
        for M in range(1, 101):
            reps = 100 - M + 1
            forward_lst_col = []
            for j in range(reps):
                forward_lst_col2 = []
                for l in range(M):
                    forward_lst_col2.append(arr[j + l][i])
                forward_lst_col.append(''.join(forward_lst_col2))

            for k in range(len(forward_lst_col)):
                if forward_lst_col[k] == forward_lst_col[k][::-1]:
                    max_len.append(len(forward_lst_col[k]))

    print(f'#{tc} {max(max_len)}')
