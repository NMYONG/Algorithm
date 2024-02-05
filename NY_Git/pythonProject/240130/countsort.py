# N = 6
# K = 9 # 0 ~ K
# data = [7, 2, 4, 5, 2, 3] # 0~9, K=9
# counts = [0] * (K+1)
# temp = [0] * N
#
# # counts 배열에 기록하기
# for x in data:
#     counts[x] += 1
# # counts 누적합 구하기
# for i in range(1, K+1):
#     counts[i] += counts[i-1]
# # data의 마지막 원소부터 정렬하기
# for i in range(N-1, -1, -1): # N-1 부터 0까지
#     counts[data[i]] -= 1 # 갯수를 인덱스로 변환
#     temp[counts[data[i]]] = data[i]
#
# print(*temp)

DATA = [0, 4, 1, 3, 1, 2, 4, 1]
TEMP = [-1] * len(DATA) # 사용하지 않는 데이터로 초기화 (-1)

N = len(DATA)
K = 4 + 1 # DATA에 있는 가장 큰 값 + 1
COUNTS = [0] * K # COUNTS 초기화

# COUNTS = [1, 3, 1, 1, 2] 0:1개, 1:3개, ...
for d in DATA:
    COUNTS[d] += 1

# COUNTS = [1, 4, 3, 6, 8]
# 위치 배열 : 숫자가 마지막에 자리하는 위치(인덱스x) 찾기
for i in range(1, K):
    COUNTS[i] += COUNTS[i-1]

for i in range(N-1, -1, -1):
    COUNTS[DATA[i]] -= 1
    TEMP[COUNTS[DATA[i]]] = DATA[i]

print(TEMP)


