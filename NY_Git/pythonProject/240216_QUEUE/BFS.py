def bfs(G, v, n): # 그래프G, 탐색 시작점v, 정점의 개수n
    visited = [False] * (n+1)
    queue = []
    queue.append(v)                         # 시작점 v를 큐에 삽입
    visited[v] = 1                          # 방문 확인

    while queue:                            # 큐에 데이터가 있다면
        t = queue.pop(0)                    # 첫번째 원소 반환
        print(t)                            # 방문한 노드 출력
        for i in G[t]:                      # t와 연결된 모든 정점에 대해
            if not visited[i]:              # 방문되지 않은 곳이면
                queue.append(i)             # 큐에 넣기
                visited[i] = visited[t] + 1 # n으로 부터 1만큼 이동


# 연습문제
s = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
l = list(map(int, s.split()))

N = 7  # 노드의 개수 (Node)
E = len(l)  # 경로의 개수 * 2 (Edge)
G = [[] for _ in range(N + 1)]  # 리스트는 인덱스가 0부터 시작하므로 N+1 (Graph)
# G = [[], [], [], [], [], [], [], []]

for i in range(0, E, 2):  # i = 0, 2, 4, ... 경로가 1문장으로 주어졌기 때문에
    v1 = l[i]  # vertex (정점) / v1 = 1, 1, 2, 2, 4, 5, 6, 3
    v2 = l[i + 1]  # 2, 3, 4, 5, 6, 6, 7, 7

    G[v1].append(v2)  # 방향이 있을 경우
    G[v2].append(v1)  # 방향이 없는 경우(양방향)

print(G)
bfs(G, 1, 7)