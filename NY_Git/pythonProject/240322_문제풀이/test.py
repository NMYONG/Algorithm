# 2진수 문자열을 10진수로
def binToDec(s):
    result = 0
    for c in s:
        result = result*2 + int(c)
    return result


# 10진수 문자열을 2진수로
def decToBin(intV):
    s = ''
    while intV > 0:
        s = str(intV % 2) + s
        intV //= 2
    return s

# 16진수 문자열을 2진수로
def hexToBin(hexS):
    mapping = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
               '4': '0100', '5': '0101', '6': '0110', '7': '0111',
               '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
               'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    s = ''
    for c in hexS:
        s += mapping[c]
    return s
