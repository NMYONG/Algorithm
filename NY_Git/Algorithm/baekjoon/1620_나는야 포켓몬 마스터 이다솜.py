import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dict = {}

for i in range(1, N + 1):
    name = input().rstrip()
    dict[i] = name
    dict[name] = i

for i in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(dict[int(question)])
    else:
        print(dict[question])
