# SIZE가 4라면 index가 0 1 2 3 0 1 2 3 ... 반복되어야 한다 => mod 사용

# full, empty를 구별할 수 없다.
# (rear + 1) mod SIZE == front이면 full

def isFull():
    return front == (rear+1) % SIZE

def isEmpty():
    return front == rear

def deQueue():
    global front

    if isEmpty():
        print('empty')
        return

    front = (front+1) % SIZE
    return Q[front]

def enQueue(item):
    global rear

    if isFull():
        print('full')
        return

    rear = (rear+1) % SIZE
    Q[rear] = item


SIZE = 4 # 실제로 데이터는 3개밖에 들어가지 않는다.
Q = [-1] * SIZE

front = 0 # 데이터의 앞을 가리키고 있다.
rear = 0 # 마지막 데이터를 가리키고 있다.

enQueue(10)
enQueue(20)
enQueue(30)
enQueue(40)


t = deQueue()
print(t)
print(deQueue())
print(deQueue())