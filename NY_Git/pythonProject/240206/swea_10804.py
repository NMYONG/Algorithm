T = int(input())

for tc in range(1, T+1):

    words = input()
    dic = {'b': 'd',
           'd': 'b',
           'p': 'q',
           'q': 'p'}

    lst = []
    for w in words:
        lst.append(w)

    r_lst = lst[::-1]
    answer = []
    for r in r_lst:
        answer.append(dic[r])

    result = ''.join(map(str, answer))
    print(f'#{tc} {result}')