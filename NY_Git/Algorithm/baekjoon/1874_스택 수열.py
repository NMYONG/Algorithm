cnt = 1
stack = []
ans = []

N = int(input())

for _ in range(N): # N번 실행
    num = int(input()) # 한 개씩 입력받기

    while cnt <= num: # cnt 값을 증가시키며 입력값과 비교
        stack.append(cnt)
        ans.append('+')
        cnt += 1

    if stack[-1] == num: # 마지막 스택이 입력값과 같으면
        stack.pop()
        ans.append('-')

    else:
        print('NO')
        exit()

for i in ans:
    print(i)