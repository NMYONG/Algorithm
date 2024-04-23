'''
inOrder를 거꾸로 수행한다고 생각.

출력을 보면 가운데 숫자가 루트 노드가 되고
가웃데 숫자를 기준으로 좌, 우의 가운데 숫자가 서브 트리의 루트노드가 됨
'''

def dfs(lst, level):
    midIndex = len(lst) // 2
    ans[level].append(lst[midIndex])

    if len(lst) == 1:
        return

    dfs(lst[:midIndex], level + 1)
    dfs(lst[midIndex + 1:], level + 1)

K = int(input()) # level
numList = list(map(int, input().split()))

ans = [[] for _ in range(K)]

dfs(numList, 0)

for i in ans:
    print(*i)



