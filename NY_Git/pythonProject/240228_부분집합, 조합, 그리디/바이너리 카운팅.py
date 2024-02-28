# 부분 집합 구현 (바이너리 카운팅)

arr = ['A', 'B', 'C']
n = len(arr)

def get_sub(tar):
    for i in range(n):
        if tar & 0x1: # 1비트가 1인지 확인, 110(2) & 001(2) => False
            print(arr[i], end='')
        tar >>= 1 # 오른쪽 끝 비트를 하나씩 제거

for tar in range(1<<n):
    print('{', end='')
    get_sub(tar)
    print('}')




# 도전문제 - 친구와 카페 방문
arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)

def get_count(tar):
    cnt = 0
    for i in range(n):
        if tar & 0x1:
            cnt += 1
        tar >>= 1
    return cnt

result = 0

for tar in range(1<<n): # 2**n 번 반복
    if get_count(tar) >= 2: # bit가 2개 이상 1이라면 => 2명 이상이라면
        result += 1

print(result)

