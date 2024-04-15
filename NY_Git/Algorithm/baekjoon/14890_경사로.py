N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0 # 등산로의 개수를 저장할 변수

# 가로 등산로에 대해서 검사
for i in range(N):
    flag = 0
    cnt = 0
    for a in range(0, N-1): # 정방향
        if abs(arr[i][a] - arr[i][a+1]) > 1: # 차이가 2이상이면
            cnt = 0
            continue
        if abs(arr[i][a] - arr[i][a+1]) <= 1: # 차이가 1이하이면
            cnt += 1
        pass


# 세로 등산로에 대해서 검사
for j in range(N):
    for a in range(0, N): # 정방향
        pass


#