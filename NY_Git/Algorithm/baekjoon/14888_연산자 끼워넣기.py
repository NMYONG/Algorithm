def cal(op_lst, num_lst):
    result = num_lst[0]
    for i in range(1, len(num_lst)):
        if op_lst[i - 1] == '+':
            result += num_lst[i]
        elif op_lst[i - 1] == '-':
            result -= num_lst[i]
        elif op_lst[i - 1] == '*':
            result *= num_lst[i]
        elif op_lst[i - 1] == '/':
            if result < 0:
                result = -(abs(result) // num_lst[i])
            else:
                result //= num_lst[i]
    return result

def combination(n, lst):
    global max_num, min_num

    if n == last:
        result = cal(lst, num_lst)
        if result >= max_num:
            max_num = result
        if result <= min_num:
            min_num = result

        comb_lst.append(lst)
        return

    for i in range(last):
        if not visited[i]:
            visited[i] = 1
            combination(n + 1, lst + [operator_lst[i]])
            visited[i] = 0


N = int(input())
num_lst = list(map(int, input().split()))
operator = list(map(int, input().split()))

# 조합 할 연산자 목록 만들기
operator_lst = []
for i in range(4):
    if i == 0:
        for j in range(operator[0]):
            operator_lst.append('+')
    if i == 1:
        for j in range(operator[1]):
            operator_lst.append('-')
    if i == 2:
        for j in range(operator[2]):
            operator_lst.append('*')
    if i == 3:
        for j in range(operator[3]):
            operator_lst.append('/')

last = len(operator_lst)
comb_lst = []
visited = [0] * last

max_num = -float('inf') # -10억이라 변수 선언 잘 해주기
min_num = float('inf') # 10억

combination(0, [])

print(max_num)
print(min_num)




import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)