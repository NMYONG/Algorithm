N = int(input())
arr = [input() for _ in range(N)]

for row in range(N):
    for col in range(N):
        if arr[row][col] == 1:
