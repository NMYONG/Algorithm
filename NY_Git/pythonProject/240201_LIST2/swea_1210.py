import sys
sys.stdin = open('1210.txt', 'r')

T = 10
for _ in range(1, T+1):
    N = 100
    tc = int(input())
    LADDER = [list(map(int, input().split())) for _ in range(N)]

    # 마지막 row에서 2를 찾고 위로 올라가면서 출발 위치를 찾는다.
    # 1. 마지막 row에서 2 찾기
    for col in range(N):
        if LADDER[99][col] == 2:
            break

    # 위에서 찾은 col에 대해서 아래 for문을 진행
    # 상위 for문 안으로 들여쓰기 하면 col을 찾고 종료되어버림
    # 위로 한 칸씩 이동하기
    for row in range(99, -1, -1):
        # col의 왼쪽에 1이 있으면
            if col > 0 and LADDER[row][col-1] == 1:
                # 사다리가 1인 동안 왼쪽으로 이동
                while col > 0 and LADDER[row][col-1] == 1 :
                    col -= 1
        # 오른쪽에 1이 있으면
            elif col < N-1 and LADDER[row][col+1] == 1:
                # 사다리가 1인 동안 오른쪽으로 이동
                while col < N-1 and LADDER[row][col+1] == 1 :
                    col += 1
    # for문이 종료되었을 때의 col 출력
    print(f'#{tc} {col}')