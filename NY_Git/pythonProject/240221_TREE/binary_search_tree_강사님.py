def insert(data):
    idx = 1
    while TREE[idx]: # 비어있는 노드가 나올 때 까지 > 데이터가 있는동안 실행
        if TREE[idx] > data:
            idx *= 2
        else:
            idx = idx*2 + 1
    # while이 끝나면 노드가 빈 곳을 찾았다는 뜻
    TREE[idx] = data


# 찾으면 index return, 못 찾으면 -1 return
def find(key):
    idx = 1
    while TREE[idx]: # 데이터가 있는 동안 실행
        if TREE[idx] == key:
            return idx
        if TREE[idx] < key:
            idx = idx*2 +1
        else:
            idx *= 2
    return -1

TREE = [0] * 100
for data in [9, 4, 12, 3, 6, 15, 13, 17]:
# for data in [1, 2, 3, 4, 5]: # 정렬이 되어있는 데이터를 이진탐색트리로 만들면 비효율적 (빈공간이 많이 생긴다)
    insert(data)
print(TREE)

print(find(2))
print(find(16))
print(find(5))
print(find(3))
print(find(12))
print(find(15))
# 이진 탐색 트리를 만들고 중위 순회를 돌리면 정렬된다.
