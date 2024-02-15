

for _ in range(1, 11):
    tc = int(input())
    data = list(map(int, input().split()))

    while data[-1] != 0:
        for i in range(1, 6):
            first_data = data.pop(0)

            if first_data-i > 0:
                data.append(first_data - i)
            elif first_data-i <= 0:
                data.append(0)
                break

    result = ' '.join(map(str, data))

    print(f'#{tc} {result}')
