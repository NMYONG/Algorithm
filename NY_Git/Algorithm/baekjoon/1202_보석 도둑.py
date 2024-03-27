# N, K = 보석 개수, 가방 개수
# N개 줄에 보석의 정보 M, V
# K개 줄에 가방의 크기 C

N, K = map(int, input().split())
dic = {}                                # 보석의 무게, 가치를 담을 딕셔너리
value = []                              # 보석의 가치를 오름차순 정렬 할 리스트
bag = []                                # 가방의 크기를 입력받을 리스트
answer = 0

for i in range(N):                      # 보석의 무게, 가치를 딕셔너리에 추가
    M, V = map(int, input().split())
    dic[V] = M
    value.append(V)                     # 보석의 가치 딕셔너리 추가

value.sort(reverse=True)                # 보석의 가치 내림차순 정렬

for j in range(K):                      # 가방 리스트에 입력
    C = int(input())
    bag.append(C)

# print('dic:', dic)
# print('value:', value)
# print('bag:', bag)

bag.sort(reverse=True)


v = 0                # 딕셔너리 중복 허용x, 같은 가치의 보석이 2개 있을 때 문제 발생
while bag:           # 가방의 크기보다 보석의 무게가 작거나 같으면 정답에 값 추가, 가방이 빌때까지
    if bag[0] >= dic[value[v]]:
        answer += value[v]
        bag.pop(0)
        v += 1

    else:
        v += 1


print(answer)