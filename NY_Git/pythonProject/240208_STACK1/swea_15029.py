import sys
sys.stdin = open('swea_15029.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())  # V = 노드, E = 간선

    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    S, G = map(int, input().split())


    def dfs(current, target):
        # 현재 노드를 방문했음을 표시
        visited[current] = True

        # 현재 노드와 목표 노드가 같다면 경로가 존재
        if current == target:
            return True

        # 현재 노드와 연결된 이웃 노드 확인
        for neighbor in graph[current]:
            # 이웃 노드를 방문하지 않았다면 재귀적으로 호출하여 경로 탐색
            if not visited[neighbor]:
                if dfs(neighbor, target):
                    return True

        # 목표 노드에 도달하지 못 하면
        return False


    visited = [False] * (V + 1)
    result = 1 if dfs(S, G) else 0

    print(f'#{tc} {result}')