from collections import deque

T = int(input())
for tc in range(1, T+1):
    s = input()
    lst = deque(list(s))
    cnt = 0

    while lst:
        c = lst.popleft()
        if c == '(':
            cnt += 1
            if lst and lst[0] == ')':
                lst.popleft()
        elif c == ')':
            cnt += 1

    print(f'#{tc} {cnt}')

# T = int(input())
# for test_case in range(1,T+1):
#     field = input()
#     print(f'#{test_case} {field.count("(") + field.count(")") - field.count("()")}')