N = int(input())
for _ in range(N):
    stack = []
    ps = input()
    status = 'YES'

    for i in ps:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                status = 'NO'
                break
    if stack:
        status = 'NO'

    print(status)