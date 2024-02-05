# max 함수
def f_max(lst):
    max_v = 0
    for i in lst:
        if i >= max_v:
            max_v = i
    return max_v

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    M = input()
    counts = [0] * 10

    # 어떤 숫자가 제일 많이 나왔는지 counts
    for m in [int(digit) for digit in M]:
        counts[m] += 1

    # 가장 큰 값 구하기
    max_value = f_max(counts)
    max_index = 0
    for i in range(len(counts)):
        if counts[max_index] <= counts[i]:
            max_index = i

    print('max_value:', max_value)
    print('max_index:', max_index)
    print(counts)
    print(f'#{test_case} {max_index} {max_value}')

