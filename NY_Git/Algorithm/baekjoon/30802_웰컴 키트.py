# 6가지 사이즈
# 같은 사이즈의 T장 묶음으로 주문 가능
# 펜은 P자루씩 묶음으로 주문 or 한 자루씩 주문

N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

tCount = 0
for i in size:
    if i == 0:
        continue
    elif i <= T:
        tCount += 1
    else:
        tCount += i // T + 1

print(tCount)
print(N // P, N % P)