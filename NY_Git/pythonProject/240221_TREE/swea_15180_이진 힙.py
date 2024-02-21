# 최소 힙
def minHeap_enqueue(data):
    global last

    last += 1
    TREE[last] = data

    c = last
    p = last // 2

    while p:
        if TREE[p] > TREE[c]:
            TREE[p], TREE[c] = TREE[c], TREE[p]
            c = p
            p = c // 2
        else:
            break

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    TREE = [0] * (N+1)
    last = 0

    for data in lst:
        minHeap_enqueue(data)

    # print(TREE)
    idx = N
    # print(TREE[idx])
    total_sum = 0

    while idx != 0 :
        total_sum += TREE[idx//2]
        idx = idx // 2

    print(f'#{tc} {total_sum}')