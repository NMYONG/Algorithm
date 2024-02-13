def is_valid_move(x, y, N):
    # 주어진 좌표 (x, y)가 미로 범위 내에 있는지 확인하는 함수
    return 0 <= x < N and 0 <= y < N

def find_path(maze, start, N):
    # DFS 알고리즘을 사용하여 출발지에서 목적지로 가는 경로를 찾는 함수
    stack = [start]  # 스택을 초기화하고 시작 지점을 추가
    visited = set()  # 방문한 좌표를 저장하기 위한 집합 초기화

    while stack:
        x, y = stack.pop()  # 스택에서 현재 위치를 꺼냄

        if maze[x][y] == 3:  # 도착지에 도달했을 때
            return 1

        if (x, y) not in visited:
            visited.add((x, y))  # 현재 위치를 방문한 것으로 표시

            # 현재 위치에서 이동 가능한 모든 방향을 확인
            moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

            for move in moves:
                nx, ny = move
                # 이동할 좌표가 미로 범위 내에 있고, 벽이 아닌 경우에 스택에 추가
                if is_valid_move(nx, ny, N) and maze[nx][ny] != 1:
                    stack.append((nx, ny))

    return 0  # 경로를 찾지 못한 경우


T = int(input())  # 테스트 케이스 개수

for test_case in range(1, T+1):
    N = int(input())  # 미로 크기
    maze = [list(map(int, input())) for _ in range(N)]  # 미로 정보 입력

    # 출발 지점 찾기
    start = None
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)
                break

    if start is None:
        print(f"# {test_case} error")  # 출발 지점이 없는 경우 'error' 출력
        continue

    result = find_path(maze, start, N)
    print(f"#{test_case} {result}")  # 결과 출력
