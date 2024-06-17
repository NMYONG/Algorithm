import sys
input = sys.stdin.readline

S = input() #
stack = []
for char in S:
    if char == '<': # 괄호로 시작되면 지금까지 스택의 문자열을 뒤집어서 출력, 스택에 괄호 넣어주기
        print(''.join(stack[::-1]), end = '')
        stack.clear()
        stack.append(char)
    elif char == '>': # 괄호가 끝나면 스택에 있는 문자열을 그대로 출력
        stack.append(char)
        print(''.join(stack), end = '')
        stack.clear()
    elif char == ' ' and stack[0] != '<': # 빈공간이고 스택이 시작 괄호로 시작하지 않으면
        print(''.join(stack[::-1]), end = ' ')
        stack.clear()
    else: # 모든 문자열을 순회했으면 스택에 있는 문자열 뒤집어서 출력
        stack.append(char)
print(''.join(stack[::-1]), end = '')