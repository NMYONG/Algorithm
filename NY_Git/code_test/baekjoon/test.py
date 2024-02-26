N = int(input())
lst = list(map(int, input().split()))

idx_lst = []
idx = 0
while lst:
    lst.pop(idx)
    idx_lst.append(idx+1)
    idx += lst.pop(idx)

