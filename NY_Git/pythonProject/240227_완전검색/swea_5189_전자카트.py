# 순열을 구하고, 1,2,3,4로 했으면 1만 가져오고 나머지는 버리면 됨 (?)
def per(k, midSum):
    if k == N:
        sum_v = 0
        for i in range(N-1):
            s = path[i]
            e = path[i+1]
            sum_v += ARR[s][e]

        min_arr.append(sum_v+ARR[e][0])
        return

    for i in range(N):
        if not visited[i]:
            path[k] = i
            visited[i] = True
            s = path[k-1]
            e = path[k] # i
            per(k+1, midSum + ARR[path[k-1]][i])
            visited[i] = False


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]

    path = [-1] * N # k번째 인덱스에 값을 넣을 용도
    visited = [False] * N # 중복 순열을 순열로 바꾸기 위해 방문 표시할 리스트

    # 시작점은 항상 0이기 때문에 0번째에 True, path를 0으로 설정
    visited[0] = True
    path[0] = 0      # path에 0을 넣고 시작, 시작점은 항상 0이기 때문에
    # per(1)          # -> 0으로 시작하는 애들만 살아남게 만듦 (?) 출력하면 0부터 시작하는 경우만 있음
    min_arr = []

    # 중간값 까지 구하는 경우
    per(1, 0)
    print(f'#{tc} {min(min_arr)}')



# GPT
def makePerm(n):
    if n <= 0:
        return []

    init_perm = list(range(2, n+1)) # 초기 배열
    result = []

    def make(currPerm, remaining):
        if len(remaining) == 0:
            result.append(currPerm + [1])
            return

        for i, next_element in enumerate(remaining):
            make(currPerm + [next_element], remaining[:i] + remaining[i+1:])

    make([1], init_perm)

    return result

def calculate_values(arr, data):
    result = []

    for d in data:
        total_sum = 0
        for i in range(len(d) - 1):
            start_node = d[i]
            end_node = d[i + 1]
            total_sum += arr[start_node - 1][end_node - 1]
        result.append(total_sum)

    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for i in range(N)]

    perm = makePerm(N)
    print(perm)
    result = min(calculate_values(ARR, perm))

    print(f'#{tc} {result}')
