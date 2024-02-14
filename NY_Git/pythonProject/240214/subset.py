#부분집합

# 각 부분집합 원소의 합이 t인 부분집합 찾기
def f(i, k, t):                # k개의 원소를 가진 배열 A, 부분집합의 합이 t인 경우
    global cnt
    cnt += 1
    if i == k:                 # 모든 원소에 대해 결정되면
        ss = 0                 # 부분집합 원소의 합
        for j in range(k):
            if bit[j]:         # bit[i] == True A[j]가 포함된 경우
                # print(A[j], end=' ')
                ss += A[j]
        # print(ss)
        if ss == t:            # 부분집합의 합이 t인 경우
            for j in range(k):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    else:
        # for j in range(1, -1, -1):
        #     bit[i] = j
        #     f(i+1, k, t)
            bit[i] = 1
            f(i+1, k, t)
            bit[i] = 0
            f(i+1, k, t)

N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * N                 # bit[i]는 A[i]가 부분집합에 포함되는지 표시
cnt = 0

f(0, N, 10)                   # 합이 10인 경우
print('cnt:', cnt)




# 각 부분집합 원소의 합이 t인 부분집합 찾기_백트래킹
# k개의 원소를 가진 배열 A, 부분집합의 합이 t인 경우, i-1 원소까지 고려한 합 s
def f(i, k, s, t):
    global cnt
    cnt += 1
    if i == k:                      # 모든 원소에 대해 결정되면
        if s == t:
            for j in range(k):
                if bit[j]:          # bit[i] == True A[j]가 포함된 경우
                    print(A[j], end=' ')
            print()
    elif i == k:                    # 모든 원소를 고려했으나 s != t
        return
    elif s > t:                     # 고려한 원소의 합이 t 보다 큰 경우
        return
    else:
        # for j in range(1, -1, -1):
        #     bit[i] = j
        #     f(i+1, k, s+A[j]*j, t)
        bit[i] = 1                  # 포함되는 경우
        f(i+1, k, s+A[i], t)
        bit[i] = 0                  # 포함되지 않는 경우
        f(i+1, k, s, t)

N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * N                       # bit[i]는 A[i]가 부분집합에 포함되는지 표시
cnt = 0

f(0, N, 0, 10)                      # 합이 55인 경우
print('cnt :', cnt)