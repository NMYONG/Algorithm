# 연습문제 - 괄호의 짝을 검사하는 프로그램

s = '( )( )((( )))'
#s = '((( )((((( )( )((( )( ))((( ))))))'

STACK = []
result = True
for c in s:
    if c == '(': # 왼쪽 괄호면 스택에 push
        STACK.append(c)
    elif c == ')':
        if len(STACK) > 0 and STACK.pop() == '(': # pop 할 것이 있으면, 괄호의 종류가 '('이면
            # temp = STACK.pop() # 마지막 괄호를 버림 pop(-1)
            # if temp == '(': # 괄호의 종류가 '('일 경우
            continue
        else:
            result = False
            break
if len(STACK) > 0: # '('가 남아있으면
    result = False