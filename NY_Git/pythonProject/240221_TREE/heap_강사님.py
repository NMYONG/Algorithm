# 최대 힙 = 부모가 자식보다 크다
# 최소 힙 = 자식이 부모보다 크다

# left, right 크기는 비교하지 않는다

# 최대 힙 - 삽입
def enqueue(data):
    global last

    last += 1 # last = 1 (루트 노드의 주소)
    TREE[last] = data # 루트 노드의 원소

    c = last # 자식 노드의 주소
    p = last // 2 # 부모 노드의 주소

    while p:
        if TREE[p] < TREE[c]:
            TREE[p], TREE[c] = TREE[c], TREE[p]

            # 다음에 자리를 바꿔줄 p, c의 주소 재설정
            c = p
            p = c // 2
        else: # p의 값이 더 크다
            break


# 루트에 있는 원소 제거
def dequeue():
    global last

    result = TREE[1] # 루트

    # 힙을 재구성
    # 마지막 노드의 원소를 루트 노드에 넣는다
    TREE[1] = TREE[last]

    # last를 앞으로 이동
    last -= 1

    p = 1
    c = p*2

    # 좌, 우 중에서 어떤 것을 c로 할지?
    while c <= last: # 마지막 주소의 인덱스가 있을때 까지 반복
        if c+1 <= last and TREE[c] < TREE[c+1]: # 오른쪽 노드의 원소가 더 크다면
            c += 1 # 자식 노드를 오른쪽으로 설정
        if TREE[p] < TREE[c]: # 자식노드가 부모노드보다 크다면
            TREE[p], TREE[c] = TREE[c], TREE[p] # 위치 변경

            p = c # 위치 변경 했으니 주소도 변경
            c = p*2

        else:
            break

    # print(last, TREE)
    return result


TREE = [0] * 100 # 원소가 들어있지 않다면 0, 미리 빈 자리를 만들어 둠
last = 0
for data in [20, 15, 21, 4, 13, 10]:
    enqueue(data)

print(TREE)

print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
