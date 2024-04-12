N = int(input())
num_lst = [int(input()) for _ in range(N)]

num_lst.sort()

# 산술평균
print(round(sum(num_lst)/len(num_lst)))

# 중앙값
print(num_lst[len(num_lst)//2])

# 최빈값
frequency = {}
for num in num_lst:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

max_num = max(frequency.values())
max_lst = []

for i in frequency:
    if max_num == frequency[i]:
        max_lst.append(i)

if len(max_lst) > 1:
    print(max_lst[1])
else:
    print(max_lst[0])

# 범위
print(max(num_lst) - min(num_lst))