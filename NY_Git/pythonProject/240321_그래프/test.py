'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

from heapq import heappop, heappush


def dijkstra(start):
    pq = []

    # 시작점의 weight, node 번호를 저장
    heappush(pq, (0, start))
    distance[start] = 0  # 노드 초기화

    while pq:
        # 최단 거리 노드에 대한 정보 꺼내기
        dist, now = heappop(pq)

        # pq의 특성 때문에 더 긴 거리가 미리 저장되어 있음
        # now가 이미 더 짧은 거리로 온 적이 있다면 pass
        # 현재 노드가 이미 처리됐다면 skip
        if distance[now] < dist:
            continue

        # now에서 인접한 노드 확인
        for next_dist, next_node in graph[now]:
            # next_dist = to[0]
            # next_node = to[1]

            # 누적거리 계산
            new_dist = dist + next_dist

            # 이미 더 짧은 거리로 간 경우 pass
            if new_dist >= distance[next_node]:
                continue

            # 누적 거리를 최단 거리로 갱신
            distance[next_node] = new_dist
            # next_node의 인접 노드들을 pq에 추가
            heappush(pq, (new_dist, next_node))

INF = int(1e9)

V, E = map(int, input().split())
start = 0  # 시작 노드 번호

# 인접 리스트
graph = [[] for _ in range(V)]
# 누적거리를 저장할 변수
distance = [INF] * V

# 인접 리스트에 간선 정보 저장
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])

dijkstra(0)
print(distance)