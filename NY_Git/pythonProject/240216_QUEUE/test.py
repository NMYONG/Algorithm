# 후위 연산자로 변경

expression = input()



def getPostfit(s):
    stack = []
    result = []

    # 여는 괄호 '('는 스택에 들어갈 때는 다른 연산자보다 낮은 우선순위여야 하므로 isp에서는 0으로 설정
    icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
    # 다른 연산자가 여는 괄호를 만났을 때 스택에 넣을 때는, 스택 안에 있는 다른 연산자들보다 더 높은 우선순위를 가지게 되어야
    isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

    for c in s:
        if c.isdigit() or c.isalpha(): # 숫자인 경우
            result.append(c)
        elif c == ')':
            while stack [-1] != '(': # ( 나올 때 까지 pop해서 result에 추가
                result.append(stack.pop())
            stack.pop()
        else: # 연산자인 경우 peak와 비교해서 높으면 스택에 push
            if stack and isp[stack[-1]] < icp[c]:
                stack.append(c)
            else: # peak와 비교해서 낮거나 같으면 pop해서 result에 append
                while stack and isp[stack[-1]] >= icp[c]:
                    result.append(stack.pop())
                stack.append(c)

    while stack:
        result.append(stack.pop())

    answer = ''.join(result)

    return answer


print(getPostfit(expression))
