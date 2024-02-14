# T = int(input())
#
# for tc in range(1,T+1):
#     code = input()
#
#     STACK = []
#     for c in code:
#         if c == '(' or c == '{':
#             STACK.append(c)
#         elif c == ')' or c == '}':
#             if len(STACK) > 0 and STACK[-1] == '(':
#                 STACK.pop()
#             elif len(STACK) > 0 and STACK[-1] == '{':
#                 STACK.pop()
#
#
#     if len(STACK) > 0:
#         result = 0
#     else:
#         result = 1
#
#     print(f'#{tc} {result}')



T = int(input())

for tc in range(1, T+1):
    code = input()

    STACK = []
    result = 1  # 기본적으로 올바른 괄호라고 가정

    for c in code:
        if c in '({':
            STACK.append(c) # 여는 괄호일 경우 스택 추가
        elif c in ')}':
            if len(STACK) > 0:
                top = STACK.pop() # 마지막 원소 꺼냄
                if (c == ')' and top != '(') or (c == '}' and top != '{'): # 괄호의 쌍이 맞지 않는 경우
                    result = 0
                    break
            else: # 스택이 비어있는데 닫는 괄호가 나온 경우
                result = 0
                break

    if len(STACK) > 0:
        result = 0

    print(f'#{tc} {result}')

