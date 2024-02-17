# # 괄호가 없을 때
# s = '2+3*4/5'
#
# stack = []
# result = []
#
# pri = {'+': 1,
#        '-': 1,
#        '*': 2,
#        '/': 2}
#
# def makePostfix(s):
#     for c in s:
#         if c.isdigit():
#             result.append(c)
#         else:
#             if stack and pri[stack[-1]] < pri[c]:
#                 stack.append(c)
#             else:
#                 while stack and pri[stack[-1]] >= pri[c]:
#                     result.append(stack.pop())
#                 stack.append(c)
#
#     while stack:
#         result.append(stack.pop())
#
#     return result
#
# def calPostfix(lst):
#     stack = []
#
#     for c in lst:
#         if c.isdigit():
#             stack.append(c)
#         else:
#             v2 = stack.pop()
#             v1 = stack.pop()
#
#             stack.append(cal(int(v1), int(v2), c))
#
#     return stack.pop()
#
# def cal(v1, v2, op):
#     if op == '+':
#         return v1 + v2
#     elif op == '-':
#         return v1 - v2
#     elif op == '*':
#         return v1 * v2
#     else:
#         return v1 // v2
#
# print(calPostfix(makePostfix(s)))



# 괄호가 있을 때
s = '(6+5*(2-8)/2)'

stack = []
result = []



# 후위 연산자로 변경
def step1(s):
    result = []
    stack = []
    isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}

    for c in s:
        if c.isdigit():      # 피연산자일 때
            result.append(c)
        elif c == ')':       # 왼쪽 괄호일 때
            while stack[-1] != '(': # peak가 '('아닐때까지
                result.append(stack.pop())
            stack.pop()
        else:
            if stack and isp[stack[-1]] < icp[c]:
                stack.append(c)
            else:
                while stack and isp[stack[-1]] >= icp[c]: # stack의 연산자가 더 크거나 같을 동안
                    result.append(stack.pop())
                stack.append(c)

    while stack:
        result.append(stack.pop())

    answer = ''.join(result)

    return answer


def step2(lst):
    stack = []
    for c in lst:
        if c.isdigit():             # 숫자일 경우
            stack.append(c)
        else:                       # 숫자가 아닐 경우
            v2 = stack.pop()
            v1 = stack.pop()
            stack.append(calc(int(v1), int(v2), c))

    return stack.pop()

def calc(v1, v2, op):
    if op == '+':
        return v1 + v2
    elif op == '-':
        return v1 - v2
    elif op == '*':
        return v1 * v2
    else:
        return v1 // v2


post_order = step1(s)
print(post_order)
print(step2(post_order))