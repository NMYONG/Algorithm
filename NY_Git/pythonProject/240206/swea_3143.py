T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    len_A = len(A)
    len_B = len(B)

    for a in range(len_A):
        A[a]