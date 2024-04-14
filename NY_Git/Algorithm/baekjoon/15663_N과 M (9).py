import sys
input = sys.stdin.readline

def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return

    curr_num = 0 # 변수 초기화
    for i in range(len(numbers)):
        if visited[i] == 0 and curr_num != numbers[i]:
            visited[i] = 1
            dfs(n + 1, lst + [numbers[i]])
            curr_num = numbers[i]
            visited[i] = 0

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

ans = []
visited = [0] * len(numbers)

dfs(0, [])

for i in ans:
    print(*i)