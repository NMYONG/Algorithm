# 순열

N = 3
numbers = [10, 11, 2]

for i in range(3):

    for j in range(3):
        if j == i :
            continue

        for k in range(3):
            if k == i or k == j:
                continue

            print(i, j, k, ' > ', numbers[i], numbers[j], numbers[k])

## baby_gin

def babygin(s_numbers):
    counts = [0] * 12
    numbers = list(map(int, s_numbers))

    for n in numbers:
        counts[n] += 1

    tri, run = 0
    i = 0
    while i < 10:
        #tri
        if counts[i] >= 3:
