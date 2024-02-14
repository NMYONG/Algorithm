import sys
sys.stdin = open('1206input.txt', 'r')

test_case = 10

for i in range(1, test_case + 1):
    N = int(input())
    BUILD = list(map(int, input().split()))

    cnt = 0

    for j in range(2, N-1):
        if (BUILD[j] > BUILD[j-2] and BUILD[j] > BUILD[j-1]) \
                and (BUILD[j] > BUILD[j+2] and BUILD[j] > BUILD[j+1]):
            cnt += BUILD[j] - max(BUILD[j-2], BUILD[j-1], BUILD[j+1], BUILD[j+2])

    print(f'#{i} {cnt}')