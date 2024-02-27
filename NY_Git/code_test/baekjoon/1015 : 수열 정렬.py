# N = int(input())
# A = list(map(int, input().split()))
#
# sortA = sorted(A)
#
# P = []
# for i in range(N):
#     P.append(sortA.index(A[i]))
#     sortA[sortA.index(A[i])] = -1

N = int(input())
A = list(map(int, input().split()))

# A 오름차순으로 정렬, 각 원소가 몇 번째 인덱스에 있는지 반환
sort_A = sorted(A)

P = []
for i in range(N):
    P.append(sort_A.index(A[i]))
    sort_A[sort_A.index(A[i])] = -1 # 이미 확인한 원소는 제외

for j in P:
    print(j, end=' ')