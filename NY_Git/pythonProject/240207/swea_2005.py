T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc}')

    lst = [1] # 첫 번째 리스트 생성
    for n in range(N):
        temp_lst = [1] # 현재 행을 계산하기 위한 임시 리스트 생성
        for m in range(n - 1):
            if m < len(lst) - 1:
                temp_lst.append(lst[m] + lst[m+1])
        if n >= 1:
            temp_lst.append(1)
        lst = temp_lst

        result = ' '.join(map(str, lst))
        print(result)
