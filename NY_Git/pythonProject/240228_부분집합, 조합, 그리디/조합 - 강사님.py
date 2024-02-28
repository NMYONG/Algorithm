# 조합

def combi(k, start):
    if k == K:
        print(path)
        return

    for i in range(start, N):
        path[k] = i
        combi(k+1, i+1)

arr = ['a', 'b', 'c', 'd', 'e']

N = 5
K = 3

path = [-1] * K
combi(0, 0)