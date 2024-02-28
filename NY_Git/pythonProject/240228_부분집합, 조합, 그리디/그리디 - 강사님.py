lst = [(1,4), (3,5), (1,6), (5,7), (3,8), (5,9), (6,10), (8,11), (2,13), (12,14)]
N = len(lst)
lst.sort(key = lambda x : x[1])
idx = 0

while idx < N:
    s = lst[idx][0]
    e = lst[idx][1]
    print(s, e)
    while idx < N and e > lst[idx][0]:
        idx += 1

