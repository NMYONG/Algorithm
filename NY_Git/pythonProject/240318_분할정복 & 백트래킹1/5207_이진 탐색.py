def binarySearch(target):
    start = 0
    end = N - 1

    direction = ''

    if target in A:
        while start <= end:
            mid = (start + end) // 2

            if A[mid] == target:
                return 1

            elif A[mid] < target:
                if direction == 'right':
                    break
                direction = 'right'
                start = mid + 1

            elif A[mid] > target:
                if direction == 'left':
                    break
                direction = 'left'
                end = mid - 1

    return 0


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0

    for b in B:
        cnt += binarySearch(b)

    print(f'#{tc} {cnt}')
