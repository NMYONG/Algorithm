# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]

# min_v = 99999
#
# for i in range(N):
#     for j in range(N):
#         if i == j:
#             continue
#         team_s = arr[i][j] + arr[j][i]
#         team_l = arr[N-1-i][N-1-j] + arr[N-1-j][N-1-i]
#         gap = abs(team_s - team_l)
#
#         if gap == 0:
#             print(gap)
#             exit()
#
#         if min_v > gap:
#             min_v = gap
#
# print(min_v)


# 조합
def combi(k, start_row, start_col):
    if k == K:
        print(path)
        return

    for i in range(start_row, len(arr)):
        for j in range(start_col if i == start_row else 0, len(arr[0])):
            path[k] = (i, j)
            combi(k+1, i, j+1)

arr = [[0, 1, 2, 3, 4, 5]]  # 주어진 이중 배열
N = len(arr)  # 이중 배열의 행 수
M = len(arr[0])  # 이중 배열의 열 수
K = 3  # 팀을 이룰 인원 수

path = [-1] * K
combi(0, 0, 0)




# 강사님 풀이
def combi(k,s ):
    if k==N//2:
        값 구하기
        return

    for i in range(s, N):
        result[k] = i
        combi(k+1, )
