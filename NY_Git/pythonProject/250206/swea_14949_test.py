# 내 풀이
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    reps = N - M + 1

    # 열에 대해
    for i in range(N):
        for j in range(reps):
            forward_lst_row = arr[i][j:M+j]
            reverse_lst_row = forward_lst_row[::-1]

            if forward_lst_row == reverse_lst_row:
                answer = ''.join(forward_lst_row)

    # 행에 대해
    for i in range(N):
        forward_lst_col = []
        for j in range(reps):
            forward_lst_col2 = []
            forward_lst_col.append(forward_lst_col2)
            for l in range(M):
                forward_lst_col2.append(arr[l][j])

        for k in range(len(forward_lst_col)):
            if forward_lst_col[k] == forward_lst_col[k][::-1]:
                answer = ''.join(forward_lst_col)

    print(f'#{tc} {answer}')




# GPT 풀이
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    reps = N - M + 1

    # 열에 대해
    for i in range(N):
        for j in range(reps):
            forward_lst_row = arr[i][j:M+j]
            reverse_lst_row = forward_lst_row[::-1]

            if forward_lst_row == reverse_lst_row:
                answer = ''.join(forward_lst_row)

    # 행에 대해
    for i in range(N):
        forward_lst_col = []
        for j in range(reps):
            forward_lst_col2 = []
            for l in range(M):
                forward_lst_col2.append(arr[j+l][i])
            forward_lst_col.append(''.join(forward_lst_col2))

        for k in range(len(forward_lst_col)):
            if forward_lst_col[k] == forward_lst_col[k][::-1]:
                answer = ''.join(forward_lst_col[k])

    print(f'#{tc} {answer}')

