def is_valid_move(x, y, N):
    return 0 <= x < N and 0 <= y < N

def find_path(maze, start, N):
    stack = [start]
    visited = set()

    while stack:
        x, y = stack.pop()

        if maze[x][y] == 3:
            return 1

        if (x, y) not in visited:
            visited.add((x, y))

            moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

            for move in moves:
                nx, ny = move
                if is_valid_move(nx, ny, N) and maze[nx][ny] != 1:
                    stack.append((nx, ny))

    return 0


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]

    start = None
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)
                break

    if start is None:
        print(f"# {test_case} error")
        continue

    result = find_path(maze, start, N)
    print(f"#{test_case} {result}")