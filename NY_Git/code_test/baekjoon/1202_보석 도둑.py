# N, K = 보석 개수, 가방 개수
# N개 줄에 보석의 정보 M, V
# K개 줄에 가방의 크기 C

N, K = map(int, input().split())
dic = {}
weight = []
value = []
bag = []
answer = 0

for i in range(N):
    M, V = map(int, input().split())
    dic[V] = M
    weight.append(M)
    value.append(V)

value.sort(reverse=True)

for j in range(K):
    C = int(input())
    bag.append(C)

print(dic)
print(value)

for i in range(len(bag)):
    if bag[i] >= dic[value[i]]:
        answer += value[i]

print(answer)