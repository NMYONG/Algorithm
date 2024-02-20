# 순회
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
# 트리를 그래프 형태로 저장 한 경우
# 전위 순회
def preOrder(root):
    print(root)
    if len(TREE[root]) >= 1: # 왼쪽 자식 노드가 있으면
        preOrder(TREE[root][0])
    if len(TREE[root]) >= 2: # 오른쪽 자식 노드가 있으면
        preOrder(TREE[root][1])

# 중위 순회
def inOrder(root):
    if len(TREE[root]) >= 1:  # 왼쪽 자식 노드가 있으면
        inOrder(TREE[root][0])
    print(root)
    if len(TREE[root]) >= 2:  # 오른쪽 자식 노드가 있으면
        inOrder(TREE[root][1])

# 후위 순회
def postOrder(root):
    if len(TREE[root]) >= 1:  # 왼쪽 자식 노드가 있으면
        postOrder(TREE[root][0])
    if len(TREE[root]) >= 2:  # 오른쪽 자식 노드가 있으면
        postOrder(TREE[root][1])
    print(root)


N = int(input()) # 노드의 수
lst = list(map(int, input().split())) # 간선 정보
TREE = [[] for _ in range(N+1)]

for idx in range(0, len(lst), 2): # DFS, BFS와 같은 방식
    p = lst[idx]
    c = lst[idx+1] # 부모 > 자식 단방향 연결

    TREE[p].append(c)

print(TREE)

preOrder(1)
print()
inOrder(1)
print()
postOrder(1)






# 물리적인 자료구조 (타 언어) => 부모 노드를 인덱스로 보기
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def preOrder(root):
    if root: # 마지막 자식 노드를 가상의 트리라고 생각
        print(root)
        preOrder(left_c[root])
        preOrder(right_c[root])

def inOrder(root):
    if root: # 마지막 자식 노드를 가상의 트리라고 생각
        inOrder(left_c[root])
        print(root)
        inOrder(right_c[root])

def postOrder(root):
    if root: # 마지막 자식 노드를 가상의 트리라고 생각
        postOrder(left_c[root])
        postOrder(right_c[root])
        print(root)


N = int(input())
lst = list(map(int, input().split()))

left_c = [0] * (N+1)
right_c = [0] * (N+1)

for idx in range(0, len(lst), 2): # DFS, BFS와 같은 방식
    p = lst[idx]
    c = lst[idx+1] # 부모 > 자식 단방향 연결

    if left_c[p] == 0:
        left_c[p] = c
    else:
        right_c[p] = c

print(left_c)
print(right_c)
preOrder(1)
print()
inOrder(1)
print()
postOrder(1)





# 트리에 문자열 넣어서 값 찾기
# 가상의 TREE를 만들어서 값 비교하기 (완전 이진 트리)
# TREE를 생성하는 과정을 거치지 않아도 된다.
# 값을 찾아가기는 어렵지만 특정 상황에서 사용
def preOrder(root):
    if TREE[root]: # 데이터가 있으면 (0이 아니면, 기본 0으로 세팅)
        print(root, TREE[root])
        preOrder(root*2)
        preOrder(root*2 + 1)


s = 'TEST 순회! 테스트'
lst = list(s)
N = len(lst)
TREE = [0] * 100

for idx in range(N): # DFS, BFS와 같은 방식
    TREE[idx+1] = lst[idx]

print(TREE)
preOrder(1)