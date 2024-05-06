N = int(input())
lst = []
for _ in range(N):
    a, b = map(int, input().split())
    lst.append((a, b))

lst.sort(key=lambda x: (x[0], x[1]))

for i in lst:
    print(*i)