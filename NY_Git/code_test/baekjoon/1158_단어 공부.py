s = input()
s = s.upper()
cnt = []

lst = list(set(s))

for i in lst:
    cnt.append(s.count(i))

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(lst[cnt.index(max(cnt))])