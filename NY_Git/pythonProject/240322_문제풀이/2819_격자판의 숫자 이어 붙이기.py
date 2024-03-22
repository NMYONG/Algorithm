def dfs(row, col, start_num):
    # 기저조건: 7자리면 끝
    if len(start_num) == 7:
        result.append(start_num)
        return

    for d in range(4):
        new_row = row + dr[d]
        new_col = col + dc[d]
        if 0 <= new_row < 4 and 0 <= new_col < 4:
            dfs(new_row, new_col, start_num + arr[new_row][new_col])


T = int(input())
for tc in range(1, T + 1):
    # 격자판 저장
    # maps = [list(map(int, input().split())) for _ in range(4)]
    # 갈 때 마다 경로를 더하기 위해서 문자열로 저장
    arr = [input().split() for _ in range(4)]
    result = []

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])

    # 중복을 제거하기 위해 set 사용
    result = set(result)
    print(f'#{tc} {len(result)}')