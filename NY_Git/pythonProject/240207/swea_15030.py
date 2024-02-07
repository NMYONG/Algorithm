T = int(input())

for tc in range(1, T+1):
    s = list(input())

    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            s.pop(i)
            s.pop(i)
            i = max(0, i-1) # i인덱스를 제거하고 이전 인덱스로 돌아가서 다시 while문 시작
        else:
            i += 1

    print(f'#{tc} {len(s)}')