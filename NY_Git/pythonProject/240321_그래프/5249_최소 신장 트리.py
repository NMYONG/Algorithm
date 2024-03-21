from heapq import heappush, heappop


def prim(start):
    pq = []
    MST = [False] * (V + 1)
    sum_weight = 0

    heappush(pq, (0, start))

    while pq:
        weight, now = heappop(pq)

        if MST[now] == True:
            continue
        MST[now] = True
        sum_weight += weight

        for next_node, next_weight in graph[now]:
            if MST[next_node]:
                continue
            heappush(pq, (next_weight, next_node))
    return sum_weight


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # V = 0부터 마지막 노드의 번호
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1].append((n2, w))
        graph[n2].append((n1, w))

    print(f'#{tc} {prim(0)}')