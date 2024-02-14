# # 수업 내용
# def push(n):
#     global top
#     top += 1
#     if top == size:
#         print('Overflow!')
#     else:
#         stack[top] = n
#
# top = -1
# size = 10
# stack = [0] * 10 # 최대 10개의 원소 저장
#
# top += 1        # push(10)
# stack[top] = 10
#
# top += 1        # push(20)
# stack[top] = 20
#
# push(30)
#
# while top >= 0:
#     top -= 1
#     print(stack[top + 1])



# 강사님 설명
def push(c):
    global top
    if isFull(): # FULL이면 더 넣을 수 없으므로
        print('full-')
        return
    else:
        top += 1
        STACK[top] = c

def pop():
    global  top
    if isEmpty():
        print('empty-')
        return
    top -= 1
    return STACK[top + 1] # return 하고 top -1 할 수 없으니 return 이전에 쓰고 top + 1 해준다.

def peek(): # 마지막 원소가 무엇인지
    return STACK[top]

def isEmpty():
    if top < 0:
        print('empty')
        return True
    return False

def isFull():
    if top >= SIZE-1: # 현재 상태가 FULL이면 더 넣을 수 없음
        print('full')
        return True
    return False

SIZE = 10
STACK = [0] * SIZE
top = -1 # 아직 아무것도 넣지 않았다는 의미로 -1

push('A')
push('B')
push('C')

print(pop()) # 'C'
print(pop()) # 'B'
print(pop()) # 'A'

# top의 위치를 넘어가는 데이터는 유효하지 않은 데이터이다.





