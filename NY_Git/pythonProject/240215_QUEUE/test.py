T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    pizza_pot = [-1] * N
    pizza_cheese = {}

    # 피자번호, 치즈 매칭
    for index, value in enumerate(cheese):
        pizza_cheese[f'{index+1}'] = value

print(pizza_cheese)