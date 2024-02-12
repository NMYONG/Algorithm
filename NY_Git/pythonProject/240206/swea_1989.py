T = int(input())

for tc in range(1, T+1):
    word = input()

    lst = []
    for w in word:
        lst.append(w)

    r_lst = lst[::-1]

    if lst == r_lst:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')

