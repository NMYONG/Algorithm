# 중복이 없는 순열
def perm(k, N, K): # N개의 데이터로 K개의 순열 재귀로 만들기
    if k == K:
        print(path)
        return

    for i in range(N):
        if not visited[i]:
            path[k] = i
            visited[i] = True
            perm(k+1, N, K)
            visited[i] = False


arr = ['a', 'b', 'c', 'd', 'e']

N = 5
K = 3
path = [-1] * K

visited = [False] * N # 데이터의 사용 여부

perm(0, N, K)





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


arr = ['a', 'b', 'c', 'd', 'e']

N = 5
K = 3
path = [-1] * K

visited = [False] * N # 데이터의 사용 여부

perm(0, N, K)