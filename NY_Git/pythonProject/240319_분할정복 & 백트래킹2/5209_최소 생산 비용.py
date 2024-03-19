def dfs(level, sum_v): # 매개변수 설정(level : 깊이, sum_v : 최솟값)
    global min_sum

    # 백트래킹
    if sum_v > min_sum:
        return

    # level이 최대에 도달하면
    if level == N:
        min_sum = min(min_sum, sum_v)
        return # 최솟값 리턴

    # 열 순회 (행 순회는 매개변수 level로)
    for i in range(N):
        if visited[i] == False: # 방문하지 않았으면
            visited[i] = True # 방문표시하고
            dfs(level + 1, sum_v + arr[level][i]) # level+1(행+1), 값 더해줌
            visited[i] = False # 방문표시 해제(다음 열 순회때 방문하기 위해)



# 입력 받기
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = 9999 # 최솟값 초기화
    visited = [0] * N # 방문 배열 초기화

    dfs(0, 0)
    print(f'#{tc} {min_sum}')

