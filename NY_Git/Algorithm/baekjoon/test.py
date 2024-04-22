def dfs(n, lst):
    if n == M:
        ansList.append(lst)
        return

    for i in range(len(numList)):


N, M = map(int, input().split())
numList = sorted(list(map(int, input().split())))

ansList = []
visited = [0] * len(numList)

dfs(0, [])

for i in ansList:
    print(*i)