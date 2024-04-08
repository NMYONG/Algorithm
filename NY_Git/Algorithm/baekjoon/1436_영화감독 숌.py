N = int(input())

cnt = 0
num = 666
while True:
    if str(num).count('666') != 0: # '666'이 한 개 이상 있으면 cnt += 1
        cnt += 1

    if cnt == N:
        break

    num += 1

print(num)