import sys
input = sys.stdin.readline

# N = int(input())
# n_lst = list(map(int, input().split()))
# M = int(input())
# m_lst = list(map(int, input().split()))
#
# for i in m_lst:
#     if i in n_lst:
#         print(1)
#     else:
#         print(0)
#


N = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()
M = int(input())
m_lst = list(map(int, input().split()))
n_lst.sort()


def binarySearch(arr, N, key):
    start = 0
    end = N - 1

    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == key:
            return 1
        elif arr[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return 0

for i in m_lst:
    print(binarySearch(n_lst, N, i))