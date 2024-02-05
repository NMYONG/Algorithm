
# 델타를 이용한 2차 배열 탐색
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = 5
arr = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N: # 모서리, 가장자리인 경우 제외
                print(arr[ni][nj], end=' ')
        print()
