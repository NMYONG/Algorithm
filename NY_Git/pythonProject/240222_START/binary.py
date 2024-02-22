# # 10진수 > 2진수
#
# tar = 149
# result = []
#
# while tar != 0:
#     result.append(tar % 2)
#     tar //= 2
#
# result.reverse()
# print(result)


# 강사님 설명
s = '1010'
t = int(s)
print(t)

t = int(s, 2)
print(t)

t = int(s, 16)
print(t)


# 2진수 문자열을 10진수로
def binToDec(s):
    result = 0
    for c in s:
        result = result*2 + int(c)
    return result
'''
2348 = ((2*10+3)*10+4)*10+8
'''

# 10진수 문자열을 2진수로
def decToBin(intV):
    s = ''
    while intV > 0:
        s = str(intV % 2) + s
        intV //= 2
    return s

# 16진수 문자열을 10진수로
def hexToDec(s):
    result = 0
    for c in s:
        if c.isdigit():
            result = result * 16 + int(c)
        else:
            result = result * 16 + ord(c) - ord('A') + 10

    return result

# 10진수 문자열을 16진수로
def decToHex(intV):
    s = ''
    while intV > 0:
        r = intV % 16
        if r < 10:
            s = str(intV % 16) + s
        else:
            s = chr((r-10) + ord('A'))
        intV //= 16

    return s

# 16진수 문자열을 2진수로
# def hexToBin(s):
#     value = hexToDec(s)
#     binS = decToBin((value))
#     return binS

# def hexToBin(hexS):
#     hexS.replac('0', '0000')
#     hexS.replac('1', '0001')
#     ...
#     return hexS

def hexToBin(hexS):
    mapping = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
               '4': '0100', '5': '0101', '6': '0110', '7': '0111',
               '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
               'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    s = ''
    for c in hexS:
        s += mapping[c]
    return s

# 2진수 문자열을 16진수로
def binToHex(s):
    value = binToDec(s)
    hexS = decToHex(value)
    return hexS

s = '1010'
print(binToDec(s))
print(decToBin(25))
print()
print(hexToDec(s))
print(hexToDec('A0'))
print()
print(decToHex(160))
print()
hexS = 'AA0'
print(hexToBin(hexS))
print(hexToBin('2FA3'))