A, B, C = int(input()), int(input()), int(input())

number = str(A * B * C)

for i in range(10):
    print(number.count(str(i)))
