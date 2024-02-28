T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N = 컨테이너 수, M = 트럭 수
    weight = list(map(int, input().split())) # 화물의 무게
    capacity = list(map(int, input().split())) # 트럭의 적재용량

    weight.sort(reverse=True)
    capacity.sort(reverse=True)

    sum_weight = 0
    while len(capacity) != 0 and len(weight) != 0:
        if capacity[0] >= weight[0]:
            sum_weight += weight.pop(0)
            capacity.pop(0)
        elif capacity[0] < weight[0]: # 적재용량보다 화물의 무게가 크다면
            weight.pop(0)
        else:
            sum_weight = 0

    print(f'#{tc} {sum_weight}')