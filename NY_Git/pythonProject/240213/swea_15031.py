# Forth

def postfix_cal(string):
    stack = []

    for c in string:
        if c == '.':
            try:
                sum(stack)
            except TypeError:
                return 'error'
            return stack.pop()
        elif c.isdigit():
            stack.append(c)
        else:
            v2 = stack.pop()
            if stack:
                v1 = stack.pop()
                stack.append(cal(int(v1), int(v2), c))
            else:
                return 'error'
def cal(v1, v2, op):
    if op == '+':
        return v1 + v2
    elif op == '-':
        return v1 - v2
    elif op == '*':
        return v1 * v2
    elif op == '/':
        return v1 // v2
    else:
        pass

T = int(input())

for tc in range(1, T+1):
    lst = list(input().split())

    answer = postfix_cal(lst)

    print(f'#{tc} {answer}')