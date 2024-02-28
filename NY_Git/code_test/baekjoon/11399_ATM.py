N = int(input())
person = [i for i in range(1, N+1)]
p = list(map(int, input().split()))
p.sort()

answer = [p[0]]

for j in range(N-1):
    answer.append(answer[j]+p[j+1])

print(sum(answer))
