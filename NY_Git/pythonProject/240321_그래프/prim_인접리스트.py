'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

from heapq import heappop, heappush

def prim(start):
    # 우선순위 큐
    pq = []
    MST = [False] * V  # 최소 신장 트리에 포함되었는지 여부를 저장하는 배열
    sum_weight = 0  # 최소 비용의 합

    # 시작 노드 추가
    heappush(pq, (0, start))

    while pq:
        weight, now = heappop(pq)

        # 이미 방문한 노드면 건너뛰기
        # 탐색시간 줄이기
        if MST[now] == 1:
            continue

        # 방문 처리
        MST[now] = True # 방문했던 노드에 다른 길로 재방문 할 수가 있기 때문에
        # 최소 비용 갱신
        sum_weight += weight

        # 현재 노드와 연결된 모든 간선에 대해 탐색
        for next_node, next_weight in graph[now]:
            # 이미 방문한 노드는 스킵
            if MST[next_node] == 1:
                continue

            # 우선순위 큐에 간선 정보 추가
            heappush(pq, (next_weight, next_node))

    print(f'최소비용: {sum_weight}')

# 노드, 간선의 개수
V, E = map(int, input().split())
# 인접 리스트로 저장
graph = [[] for _ in range(V)]
for _ in range(E):
    s, e, w = map(int, input().split())
    # 양방향 간선이므로 양쪽에 모두 추가
    graph[s].append((e, w))
    graph[e].append((s, w))

prim(0)
print(graph)
