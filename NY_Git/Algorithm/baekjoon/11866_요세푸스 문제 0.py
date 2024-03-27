N, K = map(int, input().split())
lst = [i for i in range(1, N+1)]
answer = []

while lst:
    for i in range(K-1):
        lst.append(lst.pop(0))
    answer.append(lst.pop(0))

result = ', '.join(map(str, answer))
print(f'<{result}>')