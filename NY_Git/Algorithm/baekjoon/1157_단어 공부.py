# s = input()
# s = s.upper()
# cnt = []
#
# lst = list(set(s))
#
# for i in lst:
#     cnt.append(s.count(i))
#
# if cnt.count(max(cnt)) >= 2:
#     print('?')
# else:
#     print(lst[cnt.index(max(cnt))])

s = input()
s = s.upper()
cnt = []

set_s = list(set(s))

for i in set_s:
    cnt.append(s.count(i))


if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(set_s[cnt.index(max(cnt))])