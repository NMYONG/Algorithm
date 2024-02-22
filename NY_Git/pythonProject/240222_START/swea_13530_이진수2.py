T = int(input())

for tc in range(1, T + 1):
    N = float(input())

    lst = []
    sosu = []

    integer = 0
    decimal_point = 0

    while True:
        lst.append(int(N * 2))
        if N * 2 == 1:
            break
        sosu.append(round(N * 2 - int(N * 2), 3))
        N = abs(N * 2 - int(N * 2))

        if len(lst) >= 13:
            lst.append(int(N * 2))
            break

    if len(lst) < 13:
        answer = ''.join(map(str, lst))
    else:
        answer = 'overflow'

    print(f'#{tc} {answer}')
