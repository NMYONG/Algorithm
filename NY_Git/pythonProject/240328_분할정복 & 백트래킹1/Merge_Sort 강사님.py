def merge(left, right):
    new_lst = []
    lp = 0
    rp = 0
    while lp < len(left) and rp < len(right): # 구간 안에 있을 때
        if left[lp] < right[rp]:
            new_lst.append(left[lp])
            lp += 1
        else:
            new_lst.append(right[rp])
            rp += 1

    # 누가 남았든 상관 없이 new_lst에 붙이면 된다.
    # if lp < len(left):
    #     new_lst.extend(left[lp:])
    # if rp < len(right):
    #     new_lst.extend(right[rp:])
    new_lst.extend(left[lp:])
    new_lst.extend(right[rp:])

    return new_lst

def mergeSort(lst):
    if len(lst) <= 1:
        return lst

    m = len(lst) // 2
    left = mergeSort(lst[:m])
    right = mergeSort(lst[m:])

    new_lst = merge(left, right)

    return new_lst


numbers = [69, 10, 30, 2, 16, 8, 31, 22]
sorted_lst = mergeSort(numbers)
print(sorted_lst)