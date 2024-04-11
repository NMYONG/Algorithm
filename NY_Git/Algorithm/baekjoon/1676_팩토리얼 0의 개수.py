# 처음 0이 아닌 수가 나올 때까지

N = int(input())


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

number = str(factorial(N))
# print(number)
cnt = 0
for i in range(-1, -len(str(factorial(N))) - 1, -1):
    if number[i] == '0':
        cnt += 1
    else:
        break

print(cnt)
