# 강사님 코드(1)
def bfs(start):
    Q = []
    visited = [0] * (N + 1)

    Q.append(start)
    visited[start] = 1 # True 대신 1을 넣어주고

    while Q:
        v = Q.pop(0)
        print(v)

        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1 # 방문했다면 1을 더해줌

    print(visited)


# 튜플로 값 받기
def bfs(start):
    Q = []  # 빈 스택 생성
    visited = [False] * (N + 1)  # 방문하면 False -> True

    Q.append((start, 1)) # start(시작번호)를 Q에 넣음
    visited[start] = True  # 시작번호의 노드를 다시 가지 않도록 visited에 저장

    while Q:  # Q가 비어있지 않다면 계속 실행
        v, d = Q.pop(0)  # Q의 첫번째 원소 꺼내기
        print(v. d)

        for w in G[v]:  # w = G[v]에서 갈 수 있는 Node
            if not visited[w]:  # False일 때 아래 실행 ==> if visited[w] == False / 방문하지 않았다면
                Q.append(w, d+1)
                visited[w] = True  # 재방문 하지 않기 위해서 True로 설정



# 2차원 배열로 값을 받을 때
def bfs(s):
    Q = []
    visited = [0] * (N+1)

    Q.append((s, 1))
    visited[s] = True
    while Q:
        v, d = Q.pop(0)
        print(v, d)

        for w in range(N+1):
            if G[v][w] == 1 and not visited[w]:
                Q.append((w, d+1))
                visited[w] = True


N, E = map(int, input().split())
lst = list(map(int, input().split()))

# G = [[] for _ in range(N+1)]
'''
[[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]]
'''
G = [[0] * (N+1) for _ in range(N+1)]
for i in range(0, len(lst), 2):
    v1 = lst[i]
    v2 = lst[i+1]
    G[v1][v2] = 1
    G[v2][v1] = 1

# print(G)
bfs(1)

