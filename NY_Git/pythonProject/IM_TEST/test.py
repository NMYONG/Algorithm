# DFS
def dfs(start):
    STACK = []
    visited = [False] * (N+1)

    STACK.append(start)
    visited[start] = True

    while STACK:
        v = STACK.pop()
        print(v)

        for w in G[v]:
            if not visited[w]:
                STACK.append(w)
                visited[w] = True

# BFS
def bfs(start):
    Q = []
    visited = [False] * (N+1)
    Q.append(start)
    visited[start] = True
    while Q:
        v = Q.pop(0)
        print(v)

        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = True


# 전위 순회
def preOrder(root):
    print(root)
    if len(TREE[root]) >= 1:
        preOrder(TREE[root][0])
    if len(TREE[root]) >= 2:
        preOrder(TREE[root][1])

# 중위 순회
def inOrder(root):
    if len(TREE[root]) >= 1:
        inOrder(TREE[root][0])
    print(root)
    if len(TREE[root]) >= 2:
        inOrder(TREE[root][1])

# 후위 순회
def postOrder(root):
    if len(TREE[root]) >= 1:
        postOrder(TREE[root][0])
    if len(TREE[root]) >= 2:
        postOrder(TREE[root][2])
    print(root)