# data 안에 단어가 몇개 들어가는지 반환하는 함수

def solve():
    #변수하나 만들어서
    # 빈 칸(1)을 만나면 1증가
    # 벽(0)을 만나면 연속된 빈칸이 몇개였는지 확인
    # 길이가 K인 칸의 개수
    result = 0
    for i in range(N):
        #빈 칸의 개수를 세는 변수
        cnt = 0
        for j in range(N):
            if data[i][j] == '1':
                cnt += 1
            else: #빈 칸이 아닌 곳을 만나면
                #이전에 빈칸의 길이가 K인지 확인
                if cnt == K:
                    result += 1
                cnt = 0 #연속된 빈칸의 개수 초기화
        #행 순회가 끝났을 때 한 번 더 검사
        if cnt == K:
            result += 1

    for i in range(N):
        #빈 칸의 개수를 세는 변수
        cnt = 0
        for j in range(N):
            if data[j][i] == '1':
                cnt += 1
            else: #빈 칸이 아닌 곳을 만나면
                #이전에 빈칸의 길이가 K인지 확인
                if cnt == K:
                    result += 1
                cnt = 0 #연속된 빈칸의 개수 초기화
        #열 순회가 끝났을 때 한 번 더 검사
        if cnt == K:
            result += 1

    return result

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    # data = [input().split() for _ in range(N)]
    data = []
    for _ in range(N):
        data.append(input().split())

    result = solve()
    print(f'#{tc} {result}')



# 내 풀이

T = int(input())
#
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     result = 0
#     for i in range(N):
#         cnt_r = 0
#         max_cnt_r = 0
#         for j in range(N):
#             if arr[i][j] == 1:
#                 cnt_r += 1
#                 if cnt_r > max_cnt_r:
#                     max_cnt_r = cnt_r
#             else:
#                 cnt_r = 0
#         if max_cnt_r == K:
#             result += 1
#
#     for j in range(N):
#         cnt_c = 0
#         max_cnt_c = 0
#         for i in range(N):
#             if arr[i][j] == 1:
#                 cnt_c += 1
#                 if cnt_c > max_cnt_c:
#                     max_cnt_c = cnt_c
#             else:
#                 cnt_c = 0
#         if max_cnt_c == K:
#             result += 1
#
#     print(f'#{tc} {result}')
