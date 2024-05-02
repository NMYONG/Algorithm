# 지울 노드와 지울 노드를 부모로 갖는 노드 -999
def dfs(delete):
    tree[delete] = -999

    for i in range(N):
        if delete == tree[i]:
            dfs(i)

N = int(input())
tree = list(map(int, input().split()))
M = int(input())

dfs(M)
count = 0

# 삭제한 노드가 아니면서 다른 노드의 부모가 아닌 원소를 찾아 +1
for i in range(N): # i = 0, 1, 2, 3, 4
    if tree[i] != -999 and i not in tree:
        count += 1

print(count)
