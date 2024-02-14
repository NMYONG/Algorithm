# 계산기2

# import sys
# sys.stdin = open('swea_1223.py', 'r')

# 후위 표현식으로 만들기
def make_postfix(s):
    for c in s:
        if c.isdigit():
            result.append(c)
        else:
            if stack and pri[stack[-1]] < pri[c]:
                stack.append(c)
            else:
                while stack and pri[stack[-1]] >= pri[c]:
                    result.append(stack.pop())
                stack.append(c)

    while stack:
        result.append(stack.pop())

    return result

# 후위 표현식 계산
def postfix_cal(lst):
    stack = []
    for c in lst:
        if c.isdigit():
            stack.append(c)
        else:
            v2 = stack.pop()
            v1 = stack.pop()

            stack.append(cal(int(v1), int(v2), c))
    return stack.pop()

# 연산자 계산
def cal(v1, v2, op):
    if op == '+':
        return v1 + v2
    else:
        return v1 * v2


for tc in range(1, 11):
    N = int(input())
    s = input()

    stack = []
    result = []

    pri = {'+': 1,
           '*': 2}

    answer = postfix_cal(make_postfix(s))

    print(f'#{tc} {answer}')