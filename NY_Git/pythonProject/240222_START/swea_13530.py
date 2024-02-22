T = int(input())

for tc in range(1, T + 1):
    N = float(input())

    lst = []
    sosu = []

    while True:
        lst.append(int(N*2))
        if N *2 == 1:
            break
        sosu.append(round(N*2 - int(N*2), 3))
        N = abs(N*2 - int(N*2))

        # answer = ''.join(lst)

        if len(lst) >= 13 or round(N*2 - int(N*2), 3) in sosu:
            lst.append(int(N * 2))
            answer = 'overflow'
            break

    print(lst)


