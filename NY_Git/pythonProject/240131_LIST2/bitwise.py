# 부분집합 생성하기
arr = [1, 2, 3]

n = len(arr) # 원소의 개수

for i in range(1 << n): # 1 << n : 부분 집합의 개수 == 2**N
    for j in range(n): # 원소의 수만큼 비트를 비교
        if i & (1 << j): # i의 j번 비트가 True인경우
            print(arr[j], end=',') # j번 원소 출력
    print()
print()


# 연습문제 2
arr = [-7, -5, 2, 3, 8, -2, 4, 6, 9]
n = len(arr)  # 원소의 개수


def f(arr, N):

    for i in range(1 << n): # 1 << n : 부분 집합의 개수
        for j in range(n): # 원소의 수만큼 비트를 비교함
            if i & (1 << j): # i의 j번 비트가 1인경우
                s += arr[j]
                print(arr[j], end=',') # j번 원소 출력
        print()
    print()