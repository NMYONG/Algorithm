def infix_to_postfix(expression):
    postfix = ''
    stack = []
    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}  # 스택 외부에서의 우선순위
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}  # 스택 내부에서의 우선순위

    for token in expression:
        # Case 1: 토큰이 열린 괄호인 경우
        if token == '(' or (token in '*/+-' and (not stack or isp.get(stack[-1], 0) < icp[token])):
            stack.append(token)
        # Case 2: 토큰이 사칙연산자이며, 스택이 비어있지 않고 스택의 우선순위가 토큰보다 크거나 같은 경우
        elif token in '*/+-' and stack and isp.get(stack[-1], 0) >= icp[token]:
            # 스택의 우선순위가 낮은 것을 모두 pop하고 토큰을 스택에 추가
            while stack and isp.get(stack[-1], 0) >= icp[token]:
                postfix += stack.pop()
            stack.append(token)
        # Case 3: 토큰이 닫힌 괄호인 경우
        elif token == ')':
            # 열린 괄호가 나올 때까지 스택에서 pop하여 출력
            while stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  # 열린 괄호 제거
        # Case 4: 토큰이 피연산자인 경우
        else:
            postfix += token

    # 스택에 남아있는 모든 연산자를 pop하여 출력
    while stack:
        postfix += stack.pop()

    return postfix

fx = '(6+5*(2-8)/2)'
result = infix_to_postfix(fx)
print(result)
