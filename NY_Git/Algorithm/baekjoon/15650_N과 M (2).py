# 풀이방법1 - 이진 트리
def dfs(n, lst):
    if n > N:
        if len(lst) == M:
            ans.append(lst)
        return

    # 선택하는 경우
    dfs(n+1, lst+[n])
    # 선택하지 않는 경우
    dfs(n+1, lst)

N, M = map(int, input().split())
ans = []
dfs(1, [])

for i in ans:
    print(*i)



# 풀이방법2 - 멀티 트리
def dfs(n, s, lst):
    if n == M:
        ans.append(lst)
        return

    for i in range(s, N+1):
        dfs(n+1, i+1, lst+[i])

N, M = map(int, input().split())
ans = []
dfs(0, 1, [])
for i in ans:
    print(*i)