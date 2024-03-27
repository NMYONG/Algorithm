num = list(map(int, input().split()))
numm = ''.join(map(str, num))

sum = 0
for n in numm:
    sum += int(n) ** 2

sum %= 10

print(sum)