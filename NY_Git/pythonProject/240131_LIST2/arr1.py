# N = int(input())
#
# # 2차원 배열 생성
# arr = [list(map(int, input().split())) for _ in range(N)]
# arr2 = [[0] * N for _ in range(N)] # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
# # 아래와 같이 작성하지 않는다
# arr3 = [[0] * N] * N
# arr3[0][0] = 1 # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]