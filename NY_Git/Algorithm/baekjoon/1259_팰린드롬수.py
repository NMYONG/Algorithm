while True:
    n = input()
    if n == '0':
        exit()


    flag = 1
    for i in range(len(n)//2):
        if n[i] == n[-i-1]:
            flag = 1
        else:
            flag = 0
            print('no')
            break

    if flag == 1:
        print('yes')