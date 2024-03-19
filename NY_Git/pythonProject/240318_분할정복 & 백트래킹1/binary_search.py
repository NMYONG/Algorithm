arr = [324, 32, 22114, 16, 28, 93, 422, 21, 316]

# 1. 정렬된 상태의 데이터
arr.sort()
print(arr)


# 2. 이진 검색 - 반복문
def binarySearch(target):
    low = 0
    high = len(arr) - 1
    # 탐색 횟수
    cnt = 0

    # 해당 숫자를 찾았거나 더이상 쪼갤 수 없을 때까지
    while low <= high:
        mid = (low + high) // 2
        cnt += 1

        if arr[mid] == target:
            return mid, cnt
        elif arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1

    # 찾지 못 하면 -1 반환
    return -1, cnt


# target의 index를 반환한다.
print(f'21 = {binarySearch(21)}')
print(f'324 = {binarySearch(324)}')
print(f'888 = {binarySearch(888)}')


# 3. 이진 검색 - 재귀함수
def binarySearch(low, high, target):
    # 기저조건(언제까지 재귀가 반복?)
    if low > high:
        return -1
    # 다음 재귀가 들어가기 전엔 무엇을 해야할까?
    # 정답 판별
    mid = (low + high) // 2
    if target == arr[mid]:
        return mid

    # 다음 재귀함수 호출(파라미터)
    if target < arr[mid]:
        return binarySearch(low, mid-1, target)

    else:
        return binarySearch(mid+1, high, target)

    # 재귀 함수에서 돌아왔을 때 어떤 작업을 해야할까?


print(f'21 = {binarySearch(0, len(arr)-1, 21)}')
print(f'324 = {binarySearch(0, len(arr)-1, 324)}')
print(f'888 = {binarySearch(0, len(arr)-1, 888)}')