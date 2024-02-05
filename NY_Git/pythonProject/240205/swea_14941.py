T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    current_cnt = 0
    max_cnt = 0
    for i in str1:
        for j in str2:
            if i == j:
                current_cnt += 1
        max_cnt = max(current_cnt, max_cnt)
        current_cnt = 0

    print(f'#{tc} {max_cnt}')