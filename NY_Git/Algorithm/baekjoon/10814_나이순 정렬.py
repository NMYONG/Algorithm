N = int(input())
lst = []
for _ in range(N):
    age, name = input().split()
    lst.append((age, name))

lst.sort(key=lambda x: int(x[0]))

for i in lst:
    print(*i)