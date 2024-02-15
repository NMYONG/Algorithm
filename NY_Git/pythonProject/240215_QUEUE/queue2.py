from collections import deque

q = []
dq = deque()

for i in range(2000000):
    dq.append(i)
print('append')

while dq:
    dq.popleft()
print('end')