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
    # priority_queue
    pq = []
    MST = [0] * V

    # 최소 비용
    sum_weight = 0

    # 시작점 추가
    # [기존 BFS] 노드 번호만 관리
    # [PRIM] 가중치가 낮으면 먼저 나와야 한다.
    # 관리해야 할 데이터 : 가중치, 노드 번호
    # 방법 1. class - 3가지 이상의 데이터를 다룰 때 좋다.
    # 방법 2. 튜플 - 데이터가 3가지 이상이 되면 복잡해진다.
    heappush(pq, (0, start))

    while pq:
        weight, now = heappop(pq)

        # 우선순위 큐의 특성 상 더 먼거릴 가는 방법이 큐에 저장이 되어있기 때문에
        # 기존에 이미 더 짧은 거리로 방문했다면 continue
        # 방문했다면 continue
        if MST[now]:
            continue

        # 방문 처리
        MST[now] = 1
        # 누적합 추가
        sum_weight += weight

        # 갈 수 있는 노드들을 보면서
        for to in range(V):
            # 갈 수 없거나 이미 방문했다면 pass
            if graph[now][to] == 0 or MST[to]:
                continue

            heappush(pq, (graph[now][to], to))

    print(f'최소비용: {sum_weight}')


V, E = map(int, input().split())
# 인접 행렬로 저장
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    s, e, w = map(int, input().split())
    # [기존] 3 -> 4로 갈 수 있다.
    # graph[3][4] = 1
    # [가중치 그래프] 3 -> 4로 가는데 31이라는 비용이 든다.
    # graph[3][4] = 31
    graph[s][e] = w
    # 무방향 그래프
    graph[e][s] = w

prim(0)