# 가로 검사
def row_check(arr):
    check = []
    for row in arr:
        if set(row) == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            check.append(1)
    if sum(check) == 9:
        return True
    else:
        return False


# 세로 검사
def col_check(arr):
    check = []
    for row in range(len(arr)):
        col_lst = []
        for col in range(len(arr)):
            col_lst.append(arr[col][row])
        if set(col_lst) == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            check.append(1)
    if sum(check) == 9:
        return True
    else:
        return False


# 사각형 검사
def square_check(arr):
    check = []
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            square_lst = []
            for row in range(r, r+3):
                for col in range(c, c+3):
                    square_lst.append(arr[row][col])
            if set(square_lst) == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                check.append(1)
    if sum(check) == 9:
        return True
    else:
        return False

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    if row_check(arr) and col_check(arr) and square_check(arr):
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')

def is_valid(arr):
    for i in range(9):
        # 가로 검사
        if set(arr[i]) != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            return False

        # 세로 검사
        col_lst = [arr[j][i] for j in range(9)]
        if set(col_lst) != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            return False

    # 사각형 검사
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            square_lst = [arr[i][j] for i in range(r, r + 3) for j in range(c, c + 3)]
            if set(square_lst) != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                return False

    return True

T = int(input())

for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    if is_valid(arr):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
