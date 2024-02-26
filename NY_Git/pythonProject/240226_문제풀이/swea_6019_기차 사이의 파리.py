T = int(input())

for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())

    t = D * F / (A + B)  # F를 먼저 곱하고 (A+B)로 나눠줘야 오차가 줄어든다.
                            # t = 250 / (A + B) * F 이렇게 풀면 오차에 F 값이 곱해져 오차가 커진다.
    print(f'#{tc} {t}')