def zero():
    lst.pop()

K = int(input())
lst = []

for _ in range(K):
    n = int(input())
    if n == 0:
        if len(lst) != 0:
            zero()
        else:
            pass
    else:
        lst.append(n)

print(sum(lst))