import sys
input = sys.stdin.readline

# N = int(input())
# lst = []
#
# for _ in range(N):
#     lst.append(int(input()))
#
# lst.sort()
# print(*lst, sep='\n')

N = int(input())
lst = [0] * ( 10000 + 1)

for _ in range(N):
    lst[int(input())] += 1

for i in range(len(lst)):
    if lst[i] != 0:
        for _ in range(lst[i]):
            print(i)