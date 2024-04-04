'''
1. for문으로 배열을 탐색하면서 블록, 웜홀, 블랙홀이 아니면 dfs 실행
    1.1 dfs는 4방향으로 진행 상,하,좌,우(1,2,3,4)

2. 상,하,좌,우 방향 별 블럭을 만났을 때 방향을 바꿔줌
    2.1 상(1) 방향일 때, 1번 블럭 만나면 하(2) 방향으로 바꿈
        하(2) 방향일 때, 1번 블럭 만나면 우(4) 방향으로 바꿈
        좌(3) 방향일 때, 1번 블럭 만나면 상(1) 방향으로 바꿈
        우(4) 방향일 때, 1번 블럭 만나면 좌(3) 방향으로 바꿈

    2.2 상(1) 방향일 때, 2번 블럭 만나면 우(4) 방향으로 바꿈
        하(2) 방향일 때, 2번 블럭 만나면 상(1) 방향으로 바꿈
        좌(3) 방향일 때, 2번 블럭 만나면 하(2) 방향으로 바꿈
        우(4) 방향일 때, 2번 블럭 만나면 좌(3) 방향으로 바꿈

    2.3 상(1) 방향일 때, 3번 블럭 만나면 좌(3) 방향으로 바꿈
        하(2) 방향일 때, 3번 블럭 만나면 상(1) 방향으로 바꿈
        좌(3) 방향일 때, 3번 블럭 만나면 우(4) 방향으로 바꿈
        우(4) 방향일 때, 3번 블럭 만나면 하(2) 방향으로 바꿈

    2.4 상(1) 방향일 때, 4번 블럭 만나면 하(2) 방향으로 바꿈
        하(2) 방향일 때, 4번 블럭 만나면 좌(3) 방향으로 바꿈
        좌(3) 방향일 때, 4번 블럭 만나면 우(4) 방향으로 바꿈
        우(4) 방향일 때, 4번 블럭 만나면 상(1) 방향으로 바꿈

    2.5 상(1) 방향일 때, 4번 블럭 만나면 하(2) 방향으로 바꿈
        하(2) 방향일 때, 4번 블럭 만나면 상(1) 방향으로 바꿈
        좌(3) 방향일 때, 4번 블럭 만나면 우(4) 방향으로 바꿈
        우(4) 방향일 때, 4번 블럭 만나면 좌(3) 방향으로 바꿈

3. 상, 하, 좌, 우 별 벽을 만났을 때 방향을 바꿔줌
    3.1 상(1) 방향일 때, 벽을 만나면 하(2) 방향으로 바꿈
        하(2) 방향일 때, 벽을 만나면 상(1) 방향으로 바꿈
        좌(3) 방향일 때, 벽을 만나면 우(4) 방향으로 바꿈
        우(4) 방향일 때, 벽을 만나면 좌(3) 방향으로 바꿈

4. 웜홀(6~10)을 만나면 다른 쌍이 있는 웜홀로 이동하고 방향 유지

5. 블랙홀(-1)을 만나면 break

* 점수 획득 조건 : 블럭을 만나거나 벽을 만남
* 시작 위치를 기억하기

* dfs 함수가 들고 다녀야 할 매개변수 => 좌표, 점수, 방향
'''


def dfs(row, col, score, direction):
    if direction == 1: # 상
        row -= 1
        col = col
    elif direction == 2: # 하
        row += 1
        col = col
    elif direction == 3: # 좌
        row = row
        col -= 1
    elif direction == 4: # 우
        row = row
        col += 1

    # 블록을 만났을 경우
    if arr[row][col] == 1: # 1번 블럭을 만난 경우
        if direction == 1:
            direction = 2
        elif direction == 2:
            direction = 4
        elif direction == 3:
            direction = 1
        elif direction == 4:
            direction = 3
        score += 1

    elif arr[row][col] == 2: # 2번 블럭을 만난 경우
        if direction == 1:
            direction = 4
        elif direction == 2:
            direction = 1
        elif direction == 3:
            direction = 2
        elif direction == 4:
            direction = 3
        score += 1

    elif arr[row][col] == 3: # 3번 블럭을 만난 경우
        if direction == 1:
            direction = 3
        elif direction == 2:
            direction = 1
        elif direction == 3:
            direction = 4
        elif direction == 4:
            direction = 2
        score += 1

    elif arr[row][col] == 4: # 4번 블럭을 만난 경우
        if direction == 1:
            direction = 2
        elif direction == 2:
            direction = 3
        elif direction == 3:
            direction = 4
        elif direction == 4:
            direction = 1
        score += 1

    elif arr[row][col] == 5: # 5번 블럭을 만난 경우
        if direction == 1:
            direction = 2
        elif direction == 2:
            direction = 1
        elif direction == 3:
            direction = 4
        elif direction == 4:
            direction = 3
        score += 1

    # if arr[row][col] in [1, 5]:  # 1번 또는 5번 블럭을 만난 경우
    #     direction = (direction + 1) % 4 if direction % 2 == 1 else (direction + 3) % 4
    #     score += 1
    #
    # elif arr[row][col] == 2:  # 2번 블럭을 만난 경우
    #     direction = (direction + 3) % 4 if direction % 2 == 1 else (direction + 1) % 4
    #     score += 1
    #
    # elif arr[row][col] == 3:  # 3번 블럭을 만난 경우
    #     direction = (direction + 2) % 4 if direction % 2 == 1 else direction
    #     score += 1
    #
    # elif arr[row][col] == 4:  # 4번 블럭을 만난 경우
    #     direction = direction if direction % 2 == 1 else (direction + 1) % 4
    #     score += 1


    # 웜홀을 만났을 경우











N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

wormhole = []
for i in range(N):
    for j in range(M):
        # 웜홀 찾기
        if arr[i][j] in [6, 7, 8, 9, 10]:
            wormhole.append((i, j, arr[i][j])) # 웜홀의 좌표와 값 입력해주기


        if arr[i][j] is 0: # 빈 공간이면
            for i in range(1, 5):
                dfs(i, j, 0, i)