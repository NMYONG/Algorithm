

import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            return -1

    def top(self):
        if not self.empty():
            return self.stack[-1]
        else:
            return -1

    def size(self):
        return len(self.stack)

    def empty(self):
        return 1 if self.size() == 0 else 0

stack = Stack()
n = int(input())
for _ in range(n):
    command = input().split()

    if command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'pop':
        print(stack.pop())
    elif command[0] == 'top':
        print(stack.top())
    elif command[0] == 'size':
        print(stack.size())
    elif command[0] == 'empty':
        print(stack.empty())