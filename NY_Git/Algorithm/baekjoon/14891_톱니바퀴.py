N = 4
gear = [[0] * 8] + [list(map(int, input())) for _ in range(N)]
K = int(input())

top = [0] * (N + 1) # 12시 방향

for _ in range(K):
    idx, d = map(int, input().split())

    # 1. idx 톱니를 회전
    tempList = [(idx, 0)]
    # 2. idx 우측방향 처리(같은 극성 나오면 탈출)
    for i in range(idx + 1, N + 1):
        # 왼쪽 3시 극성 != 오른쪽 9시 극성 => 회전후보 추가
        if gear[i-1][(top[i-1]+2) % 8] != gear[i][(top[i] + 6) % 8]:
            tempList.append((i, (i-idx) % 2))
        else: # 같은 극성이면 전달 안 됨
            break
    # 3. idx 왼쪽방향 처리
    for i in range(idx - 1, 0, -1):
        # 왼쪽 3시 극성 != 오른쪽 9시 극성 => 회전후보 추가
        if gear[i][(top[i]+2) % 8] != gear[i+1][(top[i+1] + 6) % 8]:
            tempList.append((i, (idx -i) % 2))
        else: # 같은 극성이면 전달 안 됨
            break
    # 4. 실제 회전 처리
    for i, rot in tempList:
        if rot == 0: # dix 톱니의 d와 같은 방향
            top[i] = (top[i] - d + 8) % 8
        else:
            top[i] = (top[i] + d + 8) % 8

# 점수 계산
ans = 0
tbl = [0, 1, 2, 4, 8]
for i in range(1, N+1):
    ans += gear[i][top[i]] * tbl[i]

print(ans)


