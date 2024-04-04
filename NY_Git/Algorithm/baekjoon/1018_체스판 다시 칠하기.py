N, M = map(int, input().split())
chess = [input() for _ in range(N)]

white = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]
black = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]

min_v = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        case_white = 0
        case_black = 0

        for a in range(8):
            for b in range(8):
                if chess[i + a][j + b] != white[a][b]:
                    case_white += 1
                if chess[i + a][j + b] != black[a][b]:
                    case_black += 1

        min_v = min(min_v, case_white, case_black)

print(min_v)



# # 8*8 씩 잘라서 white, black과 비교, 다르다면 cnt += 1
# for i in range(N-7):
#     for j in range(M-7):
#         sliced_chess = [row[i:i+8] for row in chess[j:j+8]]
#         # print(sliced_chess)
#         if sliced_chess != white and sliced_chess != black:
#             cnt += 1
#
# print(cnt)
