import sys
input = sys.stdin.readline

N = int(input())
num_lst = [int(input()) for _ in range(N)]

num_lst.sort()

for i in num_lst:
    print(i)