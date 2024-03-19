arr = [i for i in range(1, 4)]
path = [0] * 3

def dfs(level):
    if level == 3:
        print(*path)
        return

    # 기본 코드
    # path[level] = 1
    # dfs(level + 1)
    #
    # path[level] = 2
    # dfs(level + 1)
    #
    # path[level] = 3
    # dfs(level + 1)

    for i in range(len(arr)):
        # 가지치기 (조건 설정)
        # 갈 수 없는 경우를 조건으로 설정 (권장)
        if arr[i] in path: # visited 배열사용 : 조건) not visited[i] = 1 / 사용했다면 True로 바꿔줌, 맨 아래에서 다시 False로
            continue
        path[level] = arr[i]
        dfs(level + 1)

        # 갈 수 있는 경우를 조건으로 설정
        # if arr[i] not in path:
        #     path[level] = arr[i]
        #     dfs(level + 1)

        # 갔다와서 할 로직
        # 기존 방문 초기화
        path[level] = 0

dfs(0)







# 중복허용x
arr = [i for i in range(1, 4)]
result = [-1] * len(arr)
visited = [False] * len(arr)

def dfs(level):
    if level == len(arr):
        print(*result)
        return

    for i in range(len(arr)):
        if not visited[i]: # 방문하지 않았으면
            result[level] = arr[i]
            visited[i] = True
            dfs(level+1)
            visited[i] = False

dfs(0)


# 중복허용
arr = [i for i in range(1, 4)]
result = [-1] * len(arr)

def dfs(level):
    if level == len(arr):
        print(*result)
        return

    for i in range(len(arr)):
        result[level] = arr[i]
        dfs(level+1)

dfs(0)