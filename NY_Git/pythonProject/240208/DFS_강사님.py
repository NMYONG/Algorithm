# # 형제보다 자식을 우선 탐색 (DFS)
# # 자식보다 형제를 우선 탐색 (BFS)

# # 재귀
# s = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
# l = list(map(int, s.split()))
#
# def dfs_r(v):
#     print(v)
#     visited[v] = True
#
#     for w in G[v]:
#         if not visited[w]:
#             dfs_r(w)
#
# N = 7
# E = len(l)
#
# G = [[] for _ in range(N+1)]
#
# for i in range(0, E, 2):
#     v1 = l[i]
#     v2 = l[i+1]
#     G[v1].append(v2)
#     G[v2].append(v1)
# # print(G)
#
# visited = [False] * (N+1)
#
# dfs_r(1)



# 다음에 갈 곳을 STACK에 넣어둔다. (수업 내용이랑 다른 방식)
# 오름차순 순서는 신경쓰지 않는다.
s = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
l = list(map(int, s.split()))

def dfs(start):
    STACK = [] # 빈 스택 생성
    visited = [False] * (N+1) # 방문하면 False -> True

    STACK.append(start) # start(시작번호)를 STACK에 넣음
    visited[start] = True # 시작번호의 노드를 다시 가지 않도록 visited에 저장
    while STACK: # STACK이 비어있지 않으면
        v = STACK.pop() # STACK의 마지막 원소 꺼내기
        print(v)

        for w in G[v]: # w = G[v]에서 갈 수 있는 Node
            if not visited[w]: # False일 때 아래 실행 ==> if visited[w] == False
                STACK.append(w)
                visited[w] = True # 재방문 하지 않기 위해서 True로 설정

N = 7 # 노드의 개수 (Node)
E = len(l) # 경로의 개수 * 2 (Edge)
G = [[] for _ in range(N+1)] # 리스트는 인덱스가 0부터 시작하므로 N+1 (Graph)
# G = [[], [], [], [], [], [], [], []]

for i in range(0, E, 2): # i = 0, 2, 4, 6, ...
    v1 = l[i] # vertex (정점) / v1 = 1, 1, 2, 2, 4, 5, 6, 3
    v2 = l[i+1]                   # 2, 3, 4, 5, 6, 6, 7, 7

    G[v1].append(v2) # 방향이 있을 경우
    G[v2].append(v1) # 방향이 없는 경우(양방향)
    
print(G)
dfs(1)