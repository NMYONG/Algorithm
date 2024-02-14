# 후위 표기식
def make_postfix(s):

    for c in s:
        if c.isdigit():             # c가 숫자라면
            result.append(c)
        else:                       # c가 숫자가 아니면
            if stack and pri[stack[-1]] < pri[c]: # 우선순위 비교
                stack.append(c)
            else:
                while stack and pri[stack[-1]] >= pri[c]:
                    result.append(stack.pop())
                stack.append(c)

    while stack:
        result.append(stack.pop())

    return result

# 후위 표기식 계산
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

def cal(v1, v2, op):
    if op == '+':
        return v1 + v2

for tc in range(1, 11):
    l = int(input())
    s = input()

    stack = []
    result = []

    pri = {'+': 1}

    post_order = make_postfix(s)
    answer = postfix_cal(post_order)

    print(f'#{tc} {answer}')
