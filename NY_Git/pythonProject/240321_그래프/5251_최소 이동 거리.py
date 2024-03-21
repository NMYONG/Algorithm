from heapq import heappop, heappush

def dijkstra(start):
    pq = []
    heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heappop(pq)

        if distance[now] < dist:
            continue

        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]



INF = float('inf')

V, E = map(int, input().split())
start = 0

graph = [[] for _ in range(V)]
distance = [INF] * V

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([w, s])

