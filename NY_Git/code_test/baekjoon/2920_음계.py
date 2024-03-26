lst = list(map(int, input().split()))

num = 0

for i in range(len(lst) - 1):
    if lst[i] + 1 == lst[i + 1]:
        num += 1
    elif lst[i] - 1 == lst[i + 1]:
        num -= 1
    else:
        num += 0

if num + 1 == len(lst):
    print('ascending')
elif num - 1 == -len(lst):
    print('descending')
else:
    print('mixed')
