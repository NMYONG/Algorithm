def partial(k):
    if k == N:
        # print(result)
        sum_v = 0
        for i in range(N):
            if result[i]:
                sum_v += numbers[i]
        if sum_v >= 10:
            print(sum_v)
            print(result)
        return

    result[k] = 0
    partial(k+1)
    result[k] = 1
    partial(k+1)

numbers = [i for i in range(1, 6)]
N = len(numbers)
result = [-1] * N
partial(0)