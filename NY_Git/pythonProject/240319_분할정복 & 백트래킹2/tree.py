# arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
#
# # 정석 개발 버전
# class treeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#     def insert(self, child):
#         # 왼쪽에 삽입 시도
#         if not self.left:
#             self.left = child
#             return
#         # 오른쪽에 삽입 시도
#         if not self.right:
#             self.right = child
#             return
#         # 삽입 실패
#         return
#
#     def inOrder(self):
#         if self != None:
#             # 왼쪽이 있으면 계속 탐색
#             if self.left:
#                 self.left.inOrder()
#
#             print(self.value)
#
# # 이진 트리 만들기
# # 1. 노드 생성
# nodes = [treeNode(i) for i in range(14)]
#
# # 2. 간선 생성
# for i in range(0, len(arr), 2):
#     parent_node = arr[i]
#     child_node = arr[i+1]
#     nodes[parent_node].insert(nodes[child_node])
