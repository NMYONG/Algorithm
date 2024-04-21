N = int(input())
TREE = {}
for _ in range(N):
    root, left, right = input().split()
    TREE[root] = [left, right]

# 전위 순회
def preOrder(root):
    if root != '.':
        print(root, end='')
        preOrder(TREE[root][0])
        preOrder(TREE[root][1])

def inOrder(root):
    if root != '.':
        inOrder(TREE[root][0])
        print(root, end='')
        inOrder(TREE[root][1])

def postOrder(root):
    if root != '.':
        postOrder(TREE[root][0])
        postOrder(TREE[root][1])
        print(root, end='')

print(TREE)

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
