S = input()
l = len(S)

maxLength = 0

for i in range(len(S)): # i는 0~7
    for j in range(1, l//2): # j는 1~3
        if (i - j) < 0 or (i + j) > l:
            continue
        print(i, j)
        print((i-j), (i+j))
        print()
