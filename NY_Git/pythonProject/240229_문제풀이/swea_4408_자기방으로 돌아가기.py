# 위쪽으로 몰아주기, start/end 오름차순 정렬
# 지나온 복도에 1 추가하기
# 최댓값을 출력
import sys
sys.stdin = open('swea_4408_자기방으로 돌아가기.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    corridor = [0] * 401

    for _ in range(N):
        start, end = map(int, input().split())

        # 아랫 방을 윗 방으로 변경
        if start % 2 == 0 : start -= 1
        if end % 2 == 0: end -= 1

        # 출발 방향 일치시키기 (5, 7 > 7, 5)
        if start > end:
            start, end = end, start

        for i in range(start, end+1):
            corridor[i] += 1

    print(f'#{tc} {max(corridor)}')


