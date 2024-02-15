T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    pizza_pot = [-1] * N
    pizza_cheese = {}

    # 피자번호, 치즈 매칭
    for index, value in enumerate(cheese):
        pizza_cheese[f'{index+1}'] = value

    for _ in range(N):
        pizza_pot.pop()
        pizza_pot.insert(0, cheese.pop(0))

    while len(pizza_pot) != 1:
        if len(cheese) != 0:
            if pizza_pot[0] == 0:
                pizza_pot.pop(0)
                pizza_pot.insert(0, cheese.pop(0))
            else:
                pizza_pot.append(pizza_pot.pop(0)//2)
        else: # cheese에 값이 없을 경우
            if pizza_pot[0] == 0:
                pizza_pot.pop(0)
            else:
                pizza_pot.append(pizza_pot.pop(0)//2)


    print(cheese)
    print(pizza_pot)