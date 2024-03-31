def dfs(n, lst):
    if n == M: # 기저조건
        ans.append(lst)
        return

    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(n+1, lst+[i])
            visited[i] = 0 # 다음에 다시 사용하기 위해서

N, M = map(int, input().split())
ans = [] # 정답을 담을 리스트
visited = [0] * (N+1) # 0은 사용하지 않고 1부터 N까지

dfs(0, []) # 0, 빈 리스트로 시작
for i in ans:
    print(*i)