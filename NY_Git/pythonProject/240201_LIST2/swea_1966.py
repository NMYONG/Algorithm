def selectionSort(lst, N):
    for i in range(N-1):
        min_index = i
        for j in range(i+1, N):
            if lst[min_index] > lst[j]:
                min_index = j
        lst[min_index], lst[i] = lst[i], lst[min_index]
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    lst = list(map(int, input().split()))
    selectionSort(lst, N)

    result = ' '.join((map(str, lst)))

    print(f'#{tc} {result}')
