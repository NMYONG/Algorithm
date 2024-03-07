# # 5639 이진 검색 트리
# # 완전 이진 트리로 만들고 문제 풀이
#
# # 민영 풀이 - 인덱스 에러
# def postorder(root):
#     if root <= maxV and TREE[root] :
#         postorder(root*2)
#         postorder(root*2+1)
#         print(TREE[root])
#
# def maketree(data) :
#     idx = 1
#     while TREE[idx]:
#         if TREE[idx] > data :
#             idx = idx*2
#         else :
#             idx = idx*2+1
#     TREE[idx] = data
#
#
# lst = []
# while True:
#     try:
#         node = int(input())
#         lst.append(node)
#     except:
#         break
#
#
# maxV = max(lst)
# TREE = [0]*(2*maxV+1)
#
# # TREE = [0]*10001 #시간 많이 들어감
# for data in lst :
#     maketree(data)
# postorder(1)
#
#
#
#


# 하연 코드
# 5639번 : 이진 검색 트리 (트리, 재귀)

import sys

sys.setrecursionlimit(10000)  # 최대 재귀 횟수 1000(기존) => 최대 트리 깊이(10000)으로 변경
input = sys.stdin.readline

# lst : 전위 순회한 input 값 저장
lst = []
while True:
    try:
        ipt = int(input())
        lst.append(ipt)
    except:
        break

# 사용할 변수 선언
maxi = max(lst) + 1
left = [0] * maxi  # 트리의 왼쪽 노드
right = [0] * maxi  # 트리의 오른쪽 노드

# 트리에 노드값 담기
for i in range(1, len(lst)):
    root = lst[0]  # root 초기화
    find = False  # find : while문 중단을 위한 변수

    # 자기 자리를 찾아갈 때까지 반복
    while True:
        if lst[i] < root:  # root보다 작은 값일 경우
            if left[root] == 0:  # left가 비어있다면 저장하고 종료
                left[root] = lst[i]
                find = True
                break
            else:  # left가 비어있지 않다면 root값을 변경 => 새로운 root로 다시 반복할거임
                root = left[root]

        elif lst[i] > root:  # root보다 큰 값일 경우
            if right[root] == 0:  # right가 비어있다면 저장하고 종료
                right[root] = lst[i]
                find = True
                break
            else:  # right가 비어있지 않다면 root값 변경 => while문 다시 반복
                root = right[root]

        if find:  # 자리를 찾았다면 while문 종료
            break


# 후위순회
def postorder(t):
    if t:
        postorder(left[t])
        postorder(right[t])
        print(t)


postorder(lst[0])


# 민철 - 완전 이진 트리
