
# 최대값 반환
def solve():
    # 1. 연속해서 커지는 개수를 count
    # 2. 앞 요소랑 비교해서 내가 더 크면 +1
    # 3. 앞 요소랑 비교해서 내가 더 작으면 1
    num = 1 # 점점 커지는 개수를 저장, 연속으로 커지지 않으면 1이기 때문에
    max_num = 1  # 결과로 나올 수 있는 값 중 제일 작은 값

    for i in range(1, N): # 2번째부터 1번째와 비교
        if data[i] > data[i -1]:
            num += 1
            if max_num < num:
                max_num = num
        else: # 현재 당근이 이전 당근보다 작거나 같을 때
            # if max_num < num:
            #     max_num = num
                num = 1

    return max_num


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    result = solve()
    print(f'#{tc} {result}')