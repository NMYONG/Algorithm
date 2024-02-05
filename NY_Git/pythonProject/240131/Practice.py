# # 5*5 2차 배열의 대각선 원소의 합
#
# sumV = 0
# for i in range(N):
#     sumV += arr[i][i]
#     sumV += arr[i][N-1-i]
#
# sumV -= arr[N//2][N//2] # 가운데 중첩 값 제거



# # 각 요소에 대해 그 요소와 이웃한 요소와의 차의 절댓값 구하기
# N = 5 # 5*5 배열
# arr = [[1, 1, 1, 10, 1],
#        [2, 2, 2, 20, 1],
#        [3, 3, 3, 30, 1],
#        [3, 3, 3, 30, 1],
#        [3, 3, 3, 30, 1]]
#
# def my_ABS(n): # ABS 함수 구하기
#     return n if n>=0 else -n
#
# sumV = 0
# for row in range(N):
#     for col in range(N):
#         dr = [-1, 1, 0, 0]
#         dc = [0, 0, -1, 1]
#
#         for d in range(4):
#             newR = row + dr[d]
#             newC = col + dc[d]
#
#             if 0<=newR<N and 0<=newC<N: # 범위를 벗어난 인덱스가 있어서 조건 설정
#
#                 t = my_ABS(arr[row][col] - arr[newR][newC])
#                 sumV += t
#
# print(sumV)



# N개의 정수를 입력받아 부분집합의 합이 0이 되는 것이 존재하는지 계산하는 함수

# # for문을 사용해서
# numbers = [10, 11, 12]
# for i in [0, 1]:
#     for j in [0, 1]:
#         for k in [0, 1]:
#             # print(i, j, k)
#             print('{', end=' ')
#             if i == 1:
#                 print(numbers[0], end=' ')
#             if j == 1:
#                 print(numbers[1], end=' ')
#             if k == 1:
#                 print(numbers[2], end=' ')
#             print('}')



# 비트연산자 사용
numbers = [10, 11, 12, 13]
N = len(numbers)

cnt = 0
for i in range(2**N): # 10진수 N > 2진수 N의 갯수 (2**N => 1<<N)
    print(i, end='=>')
    sumV = 0

    for j in range(N): # 데이터의 개수만큼 반복
        # t = i & (1<<j) # (001 => 1<<0), (010 => 1<<1), (100 => 1<<2)

        if i & (1<<j): # j번째 bit가 1인 경우 (001 / 010 / 100)
            sumV += numbers[i]
            print(numbers[j], end=' ')
        # else: # j번째 bit가 0인 경우
        #     pass
    print('=', sumV)
    if sumV == 10:
        cnt += 1

print(cnt)


numbers = [10,11,12]
N = 3

for i in range(2**N):
    sumV = 0
    print(i, end='->')
    for j in range(N):
        if i&(1<<j): # 0은 False, 0을 제외한 양수 값은 모두 True
                    # j번째 bit가 1인 경우 001/010/100
            print(numbers[j], end=' ')
            sumV += numbers[j]
    print('=', sumV) # 보통 출력은 초기화한 곳과 일치하면 맞다

'''
0->= 0
1->10 = 10
2->11 = 11
3->10 11 = 21
4->12 = 12
5->10 12 = 22
6->11 12 = 23
7->10 11 12 = 33
'''

# print(7&1) # => 111 & 001, result = 001(2진수) = 1
# print(7&5) # => 111 & 101, result = 101(2진수) = 5

