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
    stack = []
    result = []

    # 여는 괄호 '('는 스택에 들어갈 때는 다른 연산자보다 낮은 우선순위여야 하므로 isp에서는 0으로 설정
    icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
    # 다른 연산자가 여는 괄호를 만났을 때 스택에 넣을 때는, 스택 안에 있는 다른 연산자들보다 더 높은 우선순위를 가지게 되어야
    isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

    for c in s:
        if c.isdigit() or c.isalpha():  # 숫자인 경우
            result.append(c)
        elif c == ')':
            while stack[-1] != '(':  # ( 나올 때 까지 pop해서 result에 추가
                result.append(stack.pop())
            stack.pop()
        else:  # 연산자인 경우 peak와 비교해서 높으면 스택에 push
            if stack and isp[stack[-1]] < icp[c]:
                stack.append(c)
            else:  # peak와 비교해서 낮거나 같으면 pop해서 result에 append
                while stack and isp[stack[-1]] >= icp[c]:
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