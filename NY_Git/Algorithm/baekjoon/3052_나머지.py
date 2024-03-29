remain_lst = []
for _ in range(10):
    num = int(input())
    remain_lst.append(num%42)

print(len(set(remain_lst)))
