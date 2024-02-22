T = int(input())
for tc in range(1, T+1):
    N, N = map(int, input().split())
    ARR = [...]

    COUNT = [[0, 0, 0] for _ in range(N)]
    for row in range(N):
        COUNT[row][0] = ARR[row].count('W')
        COUNT[row][1] = ARR[row].count('B')
        COUNT[row][2] = ARR[row].count('R')

        for li in range(...):
            for l2 in range(...):
                # print(l1, l2)
                # 0 ~ l1까지 흰색
                # l1 ~ l2까지 파란색
                # l2 ~ N-1까지 빨간색색
                pass