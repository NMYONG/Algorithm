# 리스트의 좌우 합이 같은지 확인
def isSame(lst):
    mid = len(lst) // 2
    left = sum(lst[:mid])
    right = sum(lst[mid:])

    return True if left == right else False

def solution(lst):
    if len(lst) % 2 == 0: # 짝수이면
        end = len(lst)
    else:
        end = len(lst) - 1

    while end > 0:
        start = 0
        ans = 0
        while start + end <= len(lst):
            if isSame(lst[start:start+end]):
                ans = end
                return ans
            start += 1
        end -= 2
    return 0


S = list(map(int, list(input())))
print(solution(S))
