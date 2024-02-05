T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_num = 1
    current_num = 1

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current_num += 1
            max_num = max(max_num, current_num)
        else:
            current_num = 1

    print(f'#{tc} {max_num}')