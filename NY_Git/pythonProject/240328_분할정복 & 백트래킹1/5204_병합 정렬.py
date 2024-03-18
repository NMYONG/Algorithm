# 병합
def merge(left, right):
    global cnt
    new_lst = []
    lp = 0
    rp = 0

    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            new_lst.append(left[lp])
            lp += 1
        else:
            new_lst.append(right[rp])
            rp += 1

    new_lst.extend(left[lp:])
    new_lst.extend(right[rp:])

    if left[-1] > right[-1]:
        cnt += 1

    return new_lst

# 분할
def mergeSort(lst):
    if len(lst) <= 1:
        return lst

    m = len(lst) // 2
    left = mergeSort(lst[:m])
    right = mergeSort(lst[m:])

    new_lst = merge(left, right)

    return new_lst

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0

    new_lst = mergeSort(lst)

    print(f'#{tc} {new_lst[len(new_lst)//2]} {cnt}')