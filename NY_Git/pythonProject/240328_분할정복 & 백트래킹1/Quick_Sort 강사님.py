# s,e 사이에서 s 위치인 값을 pivot으로
# 좌측에는 작은 값들이 우측에는 큰 값들을 모으고
# pivot의 위치를 반환하는 함수 partition
def partition(s, e):
    p = s
    i = s
    j = e
    while i <= j:
        while i <= j and numbers[p] >= numbers[i]:  # 피봇이랑 같은 수 나오면 그냥 왼쪽에 모으기 위해
            i += 1
        while i <= j and numbers[p] < numbers[j]:
            j -= 1
        if i < j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[p], numbers[j] = numbers[j], numbers[p]
    return j


def quick_sort(s, e):
    if s < e:
        m = partition(s, e)  # 피봇인 수가 있는 인덱스
        quick_sort(s, m - 1)
        quick_sort(m + 1, e)
    # numbers [x,x,3,x,x,x,...]  # 피봇인 3이 자기 자리를 찾아가고 왼쪽에는 그것보다 작은애들 오른쪽에는 그것보다 큰애들을 모아버림


numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
N = len(numbers)
quick_sort(0, N - 1)
print(numbers)
