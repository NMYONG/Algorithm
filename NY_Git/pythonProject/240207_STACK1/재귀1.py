def f(i, k): # i : 현재 위치, k 목표
    if i == k:
        pass
    else:
        f(i+1), k


arr = [10, 20, 30]
N = len(arr)
f(arr, N)



# 강사님 설명
# 피보나치 수
def fib_r(n):
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1
    if n < 2:
        return n

    return fib_r(n-1) + fib_r(n-2)

print(fib_r(5))
