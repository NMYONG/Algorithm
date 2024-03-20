def dfs(n, cnt, power):
    global ans

    if cnt >= ans:
        return

    if n == N:
        ans = min(ans, cnt)
        return

    # 유망한 답이 먼저 나오는 방향으로 호출
    # 교체하지 않는 경우
    if power > 0:
        dfs(n + 1, cnt, power - 1)
    # 교체하는 경우
    dfs(n + 1, cnt + 1, lst[n] - 1)


T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst[0]
    ans = N  # 모든 정류장에서 교체 할 경우 (최대값)

    # 2번 정류장에서 시작함
    # 1번 정류장에서는 교체회수 포함 x
    # 배터리 양은 1번 정류장 -1
    dfs(2, 0, lst[1] - 1)
    print(f'#{tc} {ans}')




# 1부터 시작하는 경우
def dfs(idx, cnt, power):
    if cnt >= ans: # 백트래킹
        return

    if idx == N: # 일정 레벨에 도달하면 값 갱신
        ans = min(ans, cnt)
        return

    # 유망한 답이 먼저 나오는 방향으로 호출
    # 배터리를 교체하지 않고 가는 쪽이 더 유망하다.

    # 교체하지 않는 경우 (배터리가 남아있는 경우에만 가능하다)
    if power > 0:
        dfs(idx + 1, cnt, power - 1)
    # 교체하는 경우
    dfs(idx + 1, cnt + 1, lst[idx] - 1)
    global ans



T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst[0]
    ans = N # 변수 초기화(최대 교체 가능 수는 N)

    dfs(1, 0, lst[1])
    print(f'#{tc} {ans}')
