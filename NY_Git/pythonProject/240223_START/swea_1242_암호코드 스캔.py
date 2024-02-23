mapping = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

# 16진수 > 2진수
def hexToBin(string):
    s = ''
    for c in string:
        s += mapping[c]
    return s

# 2진수 > 16진수
def binToDec(string):
    result = 0
    for c in string:
        result = result*2 + int(c)
    return result

C = int(input())

for tc in range(1, C+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    new_arr = [] # 16진수를 2진수로 변경

    for i in range(1, N):
        # row, col => 위에가 0이고 끝에서 처음 나타나는 1
        



