def binarySearch(arr, N, key):
    # 구간 초기화 (인덱스)
    start = 0
    end = N - 1

    # 검색 구간이 유효하면 반복
    while start <= end:
        middle = (start+end)//2 # 중앙 원소 인덱스
        if arr[middle] == key: # 검색 성공
            return middle
        elif arr[middle] > key: # 중앙값이 키보다 클 때
            end = middle - 1
        else:                  # 중앙값이 키보다 작을 때
            start = middle + 1
    return -1                  # 검색 실패

arr = [2, 4, 7, 9, 11, 19, 23]
N = len(arr)
print(binarySearch(arr, N, 7))
