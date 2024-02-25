T = int(input())

for tc in range(1, T+1):
    string = input()
    STACK = []

    while True:
        STACK.append(string.pop(0))
