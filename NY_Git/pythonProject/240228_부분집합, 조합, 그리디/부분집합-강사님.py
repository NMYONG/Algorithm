# 순열 데이터에 매칭하기
def printData(path):
    for idx in path:
        print(arr[idx], end=' ')
    print()

def perm(k, N, K): # N개의 데이터로 K개의 순열 재귀로 만들기
    if k == K:
        print(path)
        printData(path)
        return

    for i in range(N):
        if not visited[i]:
            path[k] = i
            visited[i] = True
            perm(k+1, N, K)
            visited[i] = False

def subSum_print(path):
    for idx in range(N):
        if path[idx]:
            print(arr[idx], end=' ')
    return

def subSet(k):
    if k == N:
        print(path)
        return

    for i in range(2):
        path[k] = i
        subSet(k+1)


arr = ['a', 'b', 'c', 'd', 'e']

N = 5
K = 3
path = [-1] * N
visited = [False] * N # 데이터의 사용 여부

# perm(0, N, K)

subSet(0)
