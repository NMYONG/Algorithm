lst = []
for i in range(9):
    lst.append(int(input()))

max_idx = lst.index(max(lst))
print(max(lst))
print(max_idx+1)
