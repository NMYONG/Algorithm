# 강사님 풀이
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]
    reps = N - M + 1

def isP(s):
    if s == s[::-1]:
        return True
    else:
        False

def solve():
    for row in range(N):
        for col_s in range(N-M+1):
            new_s = arr[row][col_s:col_s+M]
            if isP(new_s):
                return new_s

    for col in range(N):
        for row_s in range(N - M + 1):
            new_s = ''
            for ...

                if isP(new_s):
                    return new_s

    return -1




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





