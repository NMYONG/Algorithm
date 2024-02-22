mapping = {
    '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
    '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
    '0110111': 8, '0001011': 9}

C = int(input())

for tc in range(1, C +1):
    N, M = map(int, input().split())

    s = [input() for _ in range(N)]

    for i in range(N):
        try:
            start_idx = (s[i][::-1].index('1'))
            break
        except ValueError:
            pass

    # print(i, start_idx)
    data = s[i][::-1][start_idx:start_idx + 56]
    real_data = data[::-1]
    # print(real_data)

    binary_code = []
    for j in range(0, len(real_data), 7):
        binary_code.append(real_data[j:j + 7])

    # print(binary_code)

    result = []
    for k in binary_code:
        result.append(mapping[k])
    # print(result)

    odd = []
    even = []
    for l in range(len(result)):
        if l % 2 == 0:
            odd.append(result[l])
        else:
            even.append(result[l])
    # print(odd, even)

    if (sum(odd) * 3 + sum(even)) % 10 == 0:
        print(f'#{tc} {sum(odd) + sum(even)}')
    else:
        print(f'#{tc} {0}')