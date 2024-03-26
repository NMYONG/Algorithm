N, X = map(int, input().split())
lst = list(map(int, input().split()))
result = []
for i in lst:
    if X > i:
        result.append(i)

print(*result)