N = 4
gear = [[0] * 8] + [list(map(int, input())) for _ in range(N)]
top = [0] * (N + 1)  # 12시 방향 톱니의 위치를 저장할 배열

K = int(input())
for _ in range(K):
    idx, d = map(int, input().split())

    tempList = [(idx, 0)]  # 회전시킬 톱니의 후보 저장하기 위한 배열 생성

    # 오른쪽 방향에 대해서
    for i in range(idx + 1, N + 1):
        # 이전 톱니(i-1)의 12시방향 + 2 => i - 1 톱니의 오른쪽 극성
        # 비교할 현재 톱니(i)의 12시 방향 + 6 => i 톱니의 왼쪽 극성
        if gear[i - 1][(top[i - 1] + 2) % 8] != gear[i][(top[i] + 6) % 8]:  # 둘이 다르면
            tempList.append((i, (i - idx) % 2))  # i번째 톱니, 회전 방향(0 or 1)
        else:  # 극성이 다른 경우 중단
            break

    # 왼쪽 방향에 대해서
    for i in range(idx - 1, 0, -1):
        if gear[i][(top[i] + 2) % 8] != gear[i + 1][(top[i + 1] + 6) % 8]:
            tempList.append((i, (idx - 1) % 2))
        else:
            break



    # 선택한 후보들 회전시키기
    for i, rot in tempList:
        if rot == 0: # 회전하려고 선택한 톱니와 같은 방향인 경우
            top[i] = (top[i] - d + 8) % 8 # i번 톱니의 12시 방향을 가리키는 인덱스를 변경
        else:
            top[i] = (top[i] + d + 8) % 8

# 점수 계산하기
ans = 0
table = [0, 1, 2, 4, 8]
for i in range(1, N + 1): # 1번부터 N번까지의 톱니바퀴에 대해서
    ans += gear[i][top[i]] * table[i]

print(ans)