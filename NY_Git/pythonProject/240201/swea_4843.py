def selectionSort(lst, M):
    for i in range(M-1):
        min_idx = i
        for j in range(i+1, M):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[min_idx], lst[i] = lst[i], lst[min_idx]
    return lst

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 입력받은 수 리스트로
    input_lst = list(map(int, input().split()))
    M = len(input_lst)

    sorted_lst = selectionSort(input_lst, M)

    new_lst = []
    for i in range(5):
        new_lst.append(sorted_lst[-i-1])
        new_lst.append(sorted_lst[i])

    print(f'#{tc} {" ".join(map(str, new_lst))}')

