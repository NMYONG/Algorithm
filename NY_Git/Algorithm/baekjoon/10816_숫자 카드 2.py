def binSearch(lst, N, key):
    start = 0
    end = N - 1
    cnt = 0

    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == key:
            cnt += 1
            lst.remove(key)
        elif lst[mid] > key:
            end = mid - 1
        else:
            start = mid + 1


N = int(input())
hasCard = sorted(list(map(int, input().split())))
M = int(input())
checkCard = sorted(list(map(int, input().split())))
