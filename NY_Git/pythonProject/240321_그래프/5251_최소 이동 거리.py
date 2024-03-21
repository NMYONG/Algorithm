from heapq import heappop, heappush

def dijkstra(start):
    pq = []
    heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heappop(pq)

        if distance[now] < dist:
            continue

        for next_dist, next_node in graph[now]:
            new_dist = dist + next_dist

            if new_dist >= distance[next_node]:
                continue

            distance[next_node] = new_dist
            heappush(pq, (new_dist, next_node))


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    distance = [float('inf')] * (N+1)

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))

    # print(graph)
    # print(distance)
    dijkstra(0)
    print(f'#{tc} {distance[N]}')