import sys
from collections import deque

input = sys.stdin.readline


class Deque:
    def __init__(self):
        self.deque = deque()

    def push_front(self, item):
        self.deque.appendleft(item)

    def push_back(self, item):
        self.deque.append(item)

    def pop_front(self):
        if self.deque:
            return self.deque.popleft()
        else:
            return -1

    def pop_back(self):
        if self.deque:
            return self.deque.pop()
        else:
            return -1

    def size(self):
        return len(self.deque)

    def empty(self):
        if not self.deque:
            return 1
        else:
            return 0

    def front(self):
        if self.deque:
            return self.deque[0]
        else:
            return -1

    def back(self):
        if self.deque:
            return self.deque[-1]
        else:
            return -1


N = int(input())
deque = Deque()

for _ in range(N):
    command = input().split()

    if command[0] == 'push_front':
        deque.push_front(int(command[1]))
    elif command[0] == 'push_back':
        deque.push_back(int(command[1]))
    elif command[0] == 'pop_front':
        print(deque.pop_front())
    elif command[0] == 'pop_back':
        print(deque.pop_back())
    elif command[0] == 'size':
        print(deque.size())
    elif command[0] == 'empty':
        print(deque.empty())
    elif command[0] == 'front':
        print(deque.front())
    elif command[0] == 'back':
        print(deque.back())
