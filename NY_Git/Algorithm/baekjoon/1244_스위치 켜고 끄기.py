def toggle(no):
    switch[no] = (switch[no] + 1) % 2
    # if switch[no] == 1:
    #     switch[no] = 0
    # else:
    #     switch[no] == 1


def m_do(no):
    for idx in range(no, N + 1, no):
        toggle(idx)


def f_do(no):
    toggle(no)
    s = no - 1
    e = no + 1
    while s >= 1 and e <= N and switch[s] == switch[e]:
        toggle(s)
        toggle(e)
        s -= 1
        e += 1


N = int(input())

switch = [-100] + list(map(int, input().split()))

NUM = int(input())
for _ in range(NUM):
    sex, no = map(int, input().split())
    if sex == 1:
        m_do(no)
    else:
        f_do(no)

for idx in range(1, N + 1, 20):
    print(*switch[idx:idx + 20])







# 내 코드
def toggle(no):
    # if switch[no] == 1:
    #     switch[no] = 0
    # else:
    #     switch[no] = 1
    switch[no] = (switch[no] + 1) % 2


def man(no):
    for i in range(no, N + 1, no):
        toggle(i)


def woman(no):
    toggle(no)
    n = no - 1
    m = no + 1
    while n >= 1 and N >= m and switch[n] == switch[m]:
        toggle(n)
        toggle(m)

        n -= 1
        m += 1


N = int(input())
switch = [-100] + list(map(int, input().split()))
num = int(input())

for _ in range(num):
    sex, no = map(int, input().split())

    if sex == 1:
        man(no)
    else:
        woman(no)

for i in range(1, N + 1, 20):
    print(*switch[i:i + 20])
