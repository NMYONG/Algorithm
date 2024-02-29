def start():
    sold_bread = 0
    for person in customers:
        # 특정 시간에 만들 수 있는 빵의 개수
        made_break = (person // M) * K

        # 빵을 1개 팔았다
        sold_bread += 1

        # 재고 계산
        remain = made_break - sold_bread

        # 재고가 0보다 작으면 실패
        if remain < 0:
            return 'Impossible'
    return 'Possible'


T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # M초의 시간을 들여 K개의 붕어빵 제작
    customers = list(map(int, input().split()))

    customers.sort()
    result = start()

    print(f'#{tc} {result}')