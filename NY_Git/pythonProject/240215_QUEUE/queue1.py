N = 10
q = [0] * 10

front = rear = -1

rear += 1 # enQueue(10)
q[rear] = 10
rear += 1 # enQueue(20)
q[rear] = 20
rear += 1 # enQueue(30)
q[rear] = 30
print(q)

while front != rear: # 큐가 비어있지 않으면
    front += 1
    print(q[front])