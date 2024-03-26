def dfs(idx, arr):
    global answer

    # 치킨집의 개수가 M개가 되면
    if len(arr) == M:
        result = 0

        # 집들과 치킨집 사이의 거리의 최소값 구하기
        for x, y in house:
            # 최소값을 구하므로 무한대로 변수 초기화
            min_dist = float('inf')

            # 조합으로 구한 치킨집들과 집들 사이의 치킨거리 구하기
            for nx, ny in arr:
                dist = abs(x-nx) + abs(y-ny)
                min_dist = min(min_dist, dist)
            result += min_dist
        answer = min(answer, result)
        return

    # 백트래킹
    if idx == len(chicken):
        return

    # 조합, arr에 치킨집 추가
    dfs(idx + 1, arr + [chicken[idx]])
    dfs(idx + 1, arr)


# 입력
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
answer = float('inf')
chicken = []
house = []

# 치킨집, 집의 좌표 구하기
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            house.append((i, j))
        if maps[i][j] == 2:
            chicken.append((i, j))

dfs(0, [])
print(answer)