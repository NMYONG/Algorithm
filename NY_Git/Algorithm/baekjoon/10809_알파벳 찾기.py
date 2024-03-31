S = input()

for x in 'abcdefghijklmnopqrstuvwxyz':
    print(S.find(x), end=' ')





S = list(input())
c = 'abcdefghijklmnopqrstuvwxyz'

for i in c:
    if i in S:
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')