# 부분집합

def f(i, k):
    if i ==k:
        for j in range(k):
            if bit[j]:
                print(arr[j], end=' ')
        print()
    else:
        for j in range(2):
            bit[i] = j
            f(i+1, k)


N = 4
arr = [1, 2, 3, 4]
bit = [0] * N           # bit[1] : arr[i]가 부분집합에 포함되었는지 나타내는 배열

f(0, N)                 # bit[i]에 1또는 0을 채우고, N개의 원소가 결정되면 부분집합 출력

