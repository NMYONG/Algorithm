N = int(input())

scores = list(map(int, input().split()))

max_score = max(scores)

for idx in range(N):
    scores[idx] = scores[idx] / max_score * 100

print(sum(scores)/N)