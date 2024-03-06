R, C = map(int, input().split())

arr = [[[int(num)] for num in input().split()] for _ in range(R)]

for row in range(R):
    for col in range(C):
        value = arr[row][col]

        min_value = value[0]
        min_row = row
        min_col = col

        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < R and 0 <= new_col < C:
                if min_value > arr[new_row][new_col]:
                    min_value = arr[new_row][new_col]
                    min_row = new_row
                    min_col = new_col

        if min_value != value[0]:
            arr[min_row][min_col].append(value)
            value = 0

        else:
            pass
