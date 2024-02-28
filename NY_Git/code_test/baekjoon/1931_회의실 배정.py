import sys
input = sys.stdin.readline

N = int(input())

info = []
for _ in range(N):
    start, end = map(int, input().split())
    info.append((start, end))

info.sort(key=lambda x : (x[1], x[0]))
cnt = 1

# check = []
e = info[0][1]
for idx in range(N-1):

    if info[idx+1][0] >= e:
        # check.append(info[idx+1])
        e = info[idx+1][1]
        cnt += 1

# print(check)
print(cnt)