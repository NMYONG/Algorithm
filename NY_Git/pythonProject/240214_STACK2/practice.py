# 괄호가 있을 때

s = '(6+5*(2-8)/2)'

stack = []
result = []

# 스택 밖에서의 우선순위(in_comming_priority)
icp = {'+': 1,
       '-': 1,
       '*': 2,
       '/': 2,
       '(': 3}

# 스택 안에서의 우선순위(in_stack_priority)
isp = {'+': 1,
       '-': 1,
       '*': 2,
       '/': 2,
       '(': 0}
