# 1트
# N, L = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# cnt = 0 # 등산로의 개수를 저장할 변수
#
# # 가로 등산로에 대해서 검사
# for i in range(N):
#     flag = 0
#     cnt = 0
#     for a in range(0, N-1): # 정방향
#         if abs(arr[i][a] - arr[i][a+1]) > 1: # 차이가 2이상이면
#             cnt = 0
#             continue
#         if abs(arr[i][a] - arr[i][a+1]) <= 1: # 차이가 1이하이면
#             cnt += 1
#         pass
#
#
# # 세로 등산로에 대해서 검사
# for j in range(N):
#     for a in range(0, N): # 정방향
#         pass
#

#
# # 2트
# N, L = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# answer = 0
#
# # 가로로 탐색하는 경우
# for i in range(N):
#     flag = 1
#     visited = [0] * N
#     for j in range(N - 1):
#         # 평지인 경우
#         if arr[i][j] == arr[i][j + 1]:
#             continue
#
#         # 올라가는 경우 => 다음 숫자가 더 크고 그 차이가 1이하라면
#         elif (arr[i][j] < arr[i][j + 1]) and (arr[i][j + 1] - arr[i][j]) <= 1:
#             # L만큼 길이가 존재하는지 검사
#
#             status = False  # 상태를 저장할 수 있는 변수
#             # L 길이에 대해서
#             for l in range(1, L + 1): # -인덱스가 존재,,,
#                 if j + 1 - l < 0: # -인덱스가 나오면
#                     break
#                 if (arr[i][j + 1 - l] == arr[i][j + 1] - 1) and not visited[j + 1 - l]:
#                     status = True
#                     visited[j + 1 - l] = 1
#                 else:
#                     status = False
#                     flag = 0
#                     break
#             else:
#                 status = False
#                 continue
#         if status:
#             flag = 1
#
#
#         # 내려가는 경우 => 다음 숫자가 더 작고 그 차이가 1이하라면
#         elif (arr[i][j] > arr[i][j + 1]) and (arr[i][j] - arr[i][j + 1]) <= 1:
#             # L만큼 길이가 존재하는지 검사
#             status = False  # 상태를 저장할 수 있는 변수
#             # L 길이에 대해서
#             for l in range(1, L + 1):
#                 if j + l < 0:  # -인덱스가 나오면
#                     break
#                 if (arr[i][j + l] == arr[i][j] - 1) and not visited[j + l]:
#                     status = True
#                     visited[j + l] = 1
#                 else:
#                     status = False
#                     flag = 0
#                     break
#             else:
#                 status = False
#                 continue
#         if status:
#             flag = 1
#
#     # 끝까지 돌았는데 flag가 True이면 등산로를 놓을 수 있다
#     if flag:
#         answer += 1
#
# print(answer)


# 3트
# N, L = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# answer = 0
#
# # 가로로 탐색하는 경우
# for i in range(N):
#     flag = True  # 기본적으로 갈 수 있다고 생각하고 아닌 조건을 제외
#     visited = [0] * N
#     for j in range(N - 1):
#
#         # 평평한 경우
#         if arr[i][j] == arr[i][j + 1]:
#             continue
#
#         # 올라가는 경우
#         elif arr[i][j] + 1 == arr[i][j + 1]:
#             for l in range(1, L + 1):
#                 if (j + 1 - l) in range(0, N):  # 인덱스가 0 ~ N-1 사이이면
#                     if arr[i][j + 1 - l] + 1 != arr[i][j + 1] and visited[j + 1 - l]:  # 높은 곳을 기준으로 l만큼 뒤로 갔을 때 높이 비교
#                         flag = False
#                     else:
#                         visited[j + 1 - l] = 1
#                 else:  # 인덱스가 0 ~ N-1 사이가 아니라면 경사로를 만들 수 없음
#                     flag = False
#
#         # 내려가는 경우
#         elif arr[i][j] - 1 == arr[i][j + 1]:
#             for l in range(1, L + 1):
#                 if (j + l) in range(0, N):  # 인덱스가 0 ~ N-1 사이이면
#                     if arr[i][j] - 1 != arr[i][j + l] and visited[j + l]:  # 낮은 곳을 기준으로 l만큼 앞으로 갔을 때 높이 비교
#                         flag = False
#                     else:
#                         visited[j + l] = 1
#                 else:  # 인덱스가 0 ~ N-1 사이가 아니라면 경사로를 만들 수 없음
#                     flag = False
#
#         else:
#             flag = False
#
#     if flag:
#         answer += 1
#
# print(answer)



# 4트
import sys
input = sys.stdin.readline

def check(lst, L):
    visited = [False] * N
    for i in range(N - 1):

        # 평평할 때
        if lst[i] == lst[i+1]:
            continue

        # 높이차이가 1 이상이면 False
        elif abs(lst[i] - lst[i]) > 1:
            return False

        # 올라갈 때
        elif lst[i] + 1 == lst[i + 1]:


        # 내려갈 때



N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0

# 가로
for i in range(N):
    if check(i, L):
        answer += 1

# 세로
for i in range(N):
    temp = []
    for j in range(N):
        temp.append(arr[j][i])
    if check(temp, L):
        answer += 1

print(answer)






















