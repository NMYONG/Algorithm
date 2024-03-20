# 1~6 노드 존재

# 1. make_set
# 자기 자신인 대표인 6개가 리스트로 생성
def make_set(n):
    return [i for i in range(n)]


# 1~6번까지 사용 (0번 버림)
parents = make_set(7)


# 2. find_set
# 부모 노드를 보고 연결이 되어있다면 반복
# 자기 자신이 대표인 데이터를 찾을 때 까지
def find_set(x):  # x의 대표자 찾기
    # 부모가 자신이면 끝
    if parents[x] == x:
        return x

    # 위의 조건에 걸리지 않았다면 == 대표자가 따로 있다면
    return find_set(parents[x])


# 3. union
def union(x, y):
    x = find_set(x)
    y = find_set(y)

    # 이미 같은 집합에 속해있다면 continue
    if x == y:
        return

    # 다른 집합이라면 합침
    # 예) 더 작은 루트노드에 합치기
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

union(1, 3)
union(2, 3)