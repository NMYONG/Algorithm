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


def findSet(x):
    if parents[x] == x:
        return x

    # 경로 압축
    parents[x] = findSet(parents[x])
    return parents[x]


def union(x, y):
    x = findSet(x)
    y = findSet(y)

    # 같은 집합이면 pass
    if x == y:
        return
    if x < y:
        parents[y] = x
    if x > y:
        parents[x] = y


# 1. 전체 그래프를 보고 가중치가 제일 작은 간선부터 뽑자.
#    전체 간선 정보를 저장 + 가중치로 정렬

# 2. 방문 처리
#    싸이클이 발생하면 안된다. => union-find 알고리즘 활용

V, E = map(int, input().split())
# 간선 정보들을 저장
edges = []
for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append([s, e, w])

# 가중치를 기준으로 정렬
edges.sort(key=lambda x: x[2])
# 대표자 배열 (자기 자신을 바라봄)
parents = [i for i in range(V)]

cnt = 0
sum_weight = 0

# 간선들을 모두 확인
for s, e, w in edges:
    # 싸이클이 발생하면 pass
    # 이미 같은 집합에 속해 있으면 pass
    # 대표자가 같다 = 연결되어 있다.
    if findSet(s) == findSet(e):
        continue
    cnt += 1

    # 싸이클이 없으면 통과, 방문처리
    union(s, e)
    sum_weight += w

    # MST 완성, 간선의 개수 == V-1
    # 필요없는 싸이클이 발생하는 연산을 줄일 수 있다.
    if cnt == V - 1:
        break

print(f'최소비용 : {sum_weight}')
