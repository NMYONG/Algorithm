# st에서 j개의 돌 뒤집기
def do_1(st, j):
    for idx in range(st, st+j):
        if idx < N:
            rocks[idx] = (rocks[idx]+1) % 2


# st의 돌의 색으로 j개 만들기
def do_2(st, j):
    color = rocks[st]
    for idx in range(st, st+j):
        if idx < N:
            rocks[idx] = color


# st에서 j개를 값이 같으면 뒤집기
def do_3(st, j):
    s = st - 1
    e = st + 1
    for cnt in range(1, j):
        if s >= 0 and e < N and rocks[s] == rocks[e]:
            rocks[s] = (rocks[s] + 1) % 2
            rocks[e] = (rocks[e] + 1) % 2
            s -= 1
            e += 1

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    rocks = list(map(int, input().split()))

    for _ in range(M):
        i, j, w = map(int, input().split())

        if w == 1:
            do_1(i, j)
        elif w == 2:
            do_2()
        else:
            do_3()

    print(f'#{tc} {rocks}')