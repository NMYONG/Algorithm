'''
inOrder를 거꾸로 수행한다고 생각.

출력을 보면 가운데 숫자가 루트 노드가 되고
가웃데 숫자를 기준으로 좌, 우의 가운데 숫자가 서브 트리의 루트노드가 됨
'''

def dfs(lst, depth):
    mid_index = len(lst) // 2 # 리스트의 중간 인덱스 계산
    answer[depth].append(lst[mid_index]) # 현재 깊이의 answer 인덱스에 중간값 추가

    if len(lst) == 1: # 리스트의 길이가 1이면 재귀호출 중단
        return

    # 중간 인덱스 좌, 우로 나누어 재귀호출
    dfs(lst[:mid_index], depth + 1)
    dfs(lst[mid_index + 1:], depth + 1)


K = int(input()) # 깊이 입력받기

N = 2**K - 1 # 노드의 수
lst = list(map(int, input().split()))
answer = [[] for _ in range(K)]


dfs(lst, 0)
print(answer)

for i in answer:
    print(*i)