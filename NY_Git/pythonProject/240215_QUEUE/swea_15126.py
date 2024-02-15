T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    pizza_pot = [-1] * N
    cheese_lst = [[i+1, cheese[i]] for i in range(len(cheese))]

    for _ in range(N):
        pizza_pot.pop()
        pizza_pot.insert(0, cheese_lst.pop(0))

    while len(pizza_pot) == 1:
        if len(cheese_lst) != 0:
            if pizza_pot[0][-1] == 0:
                pizza_pot.pop(0)
                pizza_pot.insert(0, cheese_lst.pop(0))
            else:
                pizza_pot.append([pizza_pot[0][0], pizza_pot[0][-1]//2])
                pizza_pot.pop(0)
        else: # cheese에 값이 없을 경우
            if pizza_pot[0][-1] == 0:
                pizza_pot.pop(0)
            else:
                pizza_pot.append([pizza_pot[0][0], pizza_pot[0][-1]//2])
                pizza_pot.pop(0)

    print(f'#{tc} {pizza_pot[0][0]}')
